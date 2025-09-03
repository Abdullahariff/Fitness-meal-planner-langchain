
import streamlit as st
from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
import os

# Load environment variables (for API keys)
load_dotenv()

# Define the meal plan structure using Pydantic
class MealPlan(BaseModel):
    breakfast: str = Field(description="Meal plan for breakfast")
    lunch: str = Field(description="Meal plan for lunch")
    dinner: str = Field(description="Meal plan for dinner")
    snacks: str = Field(description="Meal plan for snacks")

# Function to generate meal plan using LangChain
def get_meal_plan(diet_preference, calories, cuisine):
    # Initialize Google Gemini LLM
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7, google_api_key=os.getenv("GOOGLE_API_KEY"))

    # Create a Pydantic output parser
    parser = PydanticOutputParser(pydantic_object=MealPlan)
    format_instructions = parser.get_format_instructions()

    # Create a prompt template for the meal planner
    prompt = ChatPromptTemplate.from_template(
        """You are a helpful meal planner. Create a one-day meal plan for {diet_preference}, calories {calories}, cuisine {cuisine}.

{format_instructions}
"""
    )

    # Create a LangChain sequence: Prompt -> LLM -> Output Parser
    chain = prompt | llm | parser

    # Invoke the chain with user inputs and format instructions
    meal_plan = chain.invoke({
        "diet_preference": diet_preference,
        "calories": calories,
        "cuisine": cuisine,
        "format_instructions": format_instructions
    })
    return meal_plan

# Main Streamlit app function
def main():
    st.set_page_config(page_title="AI Meal Planner", page_icon="🍴")
    st.title("🍴 AI Meal Planner")

    # Input fields for meal plan generation
    diet_preference = st.text_input("Diet Preference (e.g., high-protein, vegetarian, keto)", "high-protein")
    calories = st.number_input("Calories (e.g., 2000)", min_value=1000, max_value=5000, value=2000)
    cuisine = st.text_input("Cuisine (e.g., Pakistani, Italian, Mediterranean)", "Pakistani")

    # Checkbox for weekly plan option
    weekly_plan = st.checkbox("Weekly Plan (7 days)")

    # Button to trigger meal plan generation
    if st.button("Generate Meal Plan"):
        # Validate inputs
        if not diet_preference or not calories or not cuisine:
            st.warning("Please fill in all the input fields.")
        else:
            try:
                st.success(f"Generating meal plan for {diet_preference}, {calories} calories, {cuisine} cuisine...")
                
                # Generate and display meal plan based on weekly_plan checkbox
                if weekly_plan:
                    st.subheader("Your Weekly Meal Plan:")
                    for i in range(7):
                        st.markdown(f"### Day {i+1}")
                        meal_plan = get_meal_plan(diet_preference, calories, cuisine)
                        st.markdown(f"**Breakfast:** {meal_plan.breakfast}")
                        st.markdown(f"**Lunch:** {meal_plan.lunch}")
                        st.markdown(f"**Dinner:** {meal_plan.dinner}")
                        st.markdown(f"**Snacks:** {meal_plan.snacks}")
                else:
                    meal_plan = get_meal_plan(diet_preference, calories, cuisine)
                    st.subheader("Your Daily Meal Plan:")
                    st.markdown(f"**Breakfast:** {meal_plan.breakfast}")
                    st.markdown(f"**Lunch:** {meal_plan.lunch}")
                    st.markdown(f"**Dinner:** {meal_plan.dinner}")
                    st.markdown(f"**Snacks:** {meal_plan.snacks}")
            except Exception as e:
                st.error(f"Error generating meal plan: {str(e)}")
                st.info("Please check your API key and internet connection.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
