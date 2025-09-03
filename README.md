🍴 AI Meal Planner

An AI-powered fitness meal planner built with LangChain, Google Gemini API, and Streamlit.
This app generates personalized daily or weekly meal plans based on your diet preference, calorie target, and cuisine type.

🚀 Features

Generate personalized daily meal plans (Breakfast, Lunch, Dinner, Snacks).

Option to create a 7-day weekly meal plan.

Supports multiple diet types (e.g., vegetarian, keto, high-protein).

Customize calories and cuisine preference.

Built with LangChain + Gemini LLM + Streamlit UI.

🛠️ Tech Stack

Python

Streamlit
 – Web interface

LangChain
 – LLM orchestration

Google Gemini API
 – AI model

Pydantic
 – Structured output validation

dotenv
 – Environment variable management

 📂 Project Structure
.
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies
├── .env                # API keys (ignored in git)
└── README.md           # Project documentation


💡 Example
Input:

Diet Preference: high-protein

Calories: 2000

Cuisine: Pakistani

Weekly Plan: ✅

Output (sample day):

vbnet
Copy code
Breakfast: Boiled eggs with paratha and green tea  
Lunch: Grilled chicken breast with brown rice and salad  
Dinner: Chicken karahi with whole wheat roti  
Snacks: Greek yogurt with almonds  
⚠️ Notes
Requires a valid Google Gemini API key.

Internet connection is needed to call the API.

🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request.

📜 License
This project is licensed under the MIT License.

