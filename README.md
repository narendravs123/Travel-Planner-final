streamlit link : https://trip-planner-app.streamlit.app/
# Travel-Planner-final
# 🌍 AI-Powered Travel Planner

Welcome to the **AI-Powered Travel Planner**, your intelligent assistant for creating personalized, multi-day travel itineraries! Built using the power of **LangChain** and **Streamlit**, this project lets you effortlessly plan your trips with real-time weather, hotel, and budget insights.

## 🚀 Features
- 📍 Enter your **destination** and **number of days**
- 🌦️ Get **real-time weather forecasts** for your destination
- 🏨 View **hotel and attraction recommendations**
- 📅 Generate a **detailed multi-day itinerary** (morning, afternoon, evening)
- 💸 **Dynamic budget estimation** based on destination and duration
- 🎒 **Packing list suggestions** tailored to weather conditions
- 💾 Save and retrieve itineraries for future reference
- 📤 Export itineraries to **Markdown**, **HTML**, or **PDF**
- 🔥 Powered by **LangChain** with **Groq's LLaMA3 model**

## 🛠️ Technologies & Libraries
- **LangChain** – Manages LLM prompts and chains for itinerary generation
- **LangChain-Groq** – Integrates Groq's LLaMA3 model for advanced text generation
- **OpenWeatherMap API** – Provides real-time weather forecasts
- **SerpAPI** – (Optional) For fetching hotel and attraction links
- **Streamlit** – Interactive frontend for user input and display
- **Python-dotenv** – Securely manages API keys
- **Requests & JSON** – Data fetching and itinerary storage
- **Pandoc** – Converts itineraries to HTML/PDF for sharing

## 💡 How LangChain is Used
LangChain orchestrates the **natural language generation** of itineraries:
- Combines **user input** (destination, days) with **real-time weather** and **hotel data**
- Utilizes **PromptTemplate** and **LLMChain** to interact with Groq’s LLaMA3 model
- Produces a **natural, human-like itinerary** with recommendations, budgets, and packing lists

## 📂 Project Structure
travel_planner/
├── app.py # Streamlit frontend
├── langchain_helper.py # Core LangChain logic & data fetching
├── .env # Secure storage of API keys
├── data/ # Saved itineraries (JSON files)
├── Combined_Travel_Report.md # Merged markdown report
├── Combined_Travel_Report.html # HTML version of the report
└── requirements.txt # Project dependencies


🎨 System Architecture Diagram
Here’s a simple flowchart for your AI-Powered Travel Planner:
+-------------------------+
|  User Input (Streamlit) |
+-------------------------+
           |
           v
+-------------------------+
|  Fetch Weather (API)    |
|  Fetch Hotels (API)     |
+-------------------------+
           |
           v
+-------------------------+
| LangChain LLMChain with |
| Groq LLaMA3 Model       |
+-------------------------+
           |
           v
+-------------------------+
|  Generate Itinerary     |
|  Estimate Budget        |
|  Suggest Packing List   |
+-------------------------+
           |
           v
+-------------------------+
| Save Itinerary (JSON)   |
| Load Previous Plans     |
+-------------------------+
           |
           v
+-------------------------+
| Display Itinerary & UI  |
| Export to MD/HTML/PDF   |
+-------------------------+




