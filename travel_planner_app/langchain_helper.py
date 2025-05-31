import os
import json
from datetime import datetime
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

# Initialize the Groq LLM
llm = ChatGroq(temperature=0.7, model_name="llama3-8b-8192", api_key=GROQ_API_KEY)

# Directory for storing itineraries
DATA_DIR = r"C:\Users\naren\Desktop\travel_planner\travel_planner_app\data"

# Ensure the directory exists
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Function to get weather data
def get_weather_forecast(destination):
    import requests
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={destination}&units=metric&appid={OPENWEATHERMAP_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecast = [f"{item['main']['temp']}°C, {item['weather'][0]['description']}" for item in data['list'][:3]]
        return "\n".join(forecast)
    return "Weather data not available."

# Function to get hotels/attractions
def get_hotels_and_attractions(destination):
    return f"""Top Hotels & Attractions in {destination}:
- [TripAdvisor Hotels](https://www.tripadvisor.com/Search?q={destination}+hotels)
- [Travel Guides](https://www.hotels.com/go/{destination.replace(' ', '-')})
"""

# Budget estimation
def estimate_budget(destination, days):
    cost_data = {
        "Paris": {"hotel": 150, "food": 50, "activities": 30, "transport": 20},
        "New York": {"hotel": 200, "food": 60, "activities": 40, "transport": 30},
        "Tokyo": {"hotel": 130, "food": 40, "activities": 30, "transport": 25},
        "Bali": {"hotel": 80, "food": 25, "activities": 20, "transport": 15},
        "Bangalore": {"hotel": 70, "food": 20, "activities": 15, "transport": 10}
    }
    city_costs = cost_data.get(destination, {"hotel": 100, "food": 40, "activities": 30, "transport": 20})
    daily_budget = sum(city_costs.values())
    return daily_budget * days

# Generate itinerary with dynamic days and budget
def generate_full_travel_plan_with_budget(destination, days=3):
    weather = get_weather_forecast(destination)
    hotels = get_hotels_and_attractions(destination)
    
    prompt_template = PromptTemplate(
        input_variables=['destination', 'weather', 'hotels', 'days'],
        template=(
            "You are a travel assistant. Generate a detailed {days}-day itinerary for {destination}. "
            "Include: morning, afternoon, evening activities for each day; highlight must-visit spots; "
            "consider the following weather forecast:\n{weather}\n"
            "Here are hotels and attractions to consider:\n{hotels}\n"
            "Provide estimated budget and essential packing list based on weather."
        )
    )
    itinerary_chain = LLMChain(llm=llm, prompt=prompt_template)
    result = itinerary_chain.run({'destination': destination, 'weather': weather, 'hotels': hotels, 'days': days})
    
    budget = estimate_budget(destination, days)
    packing_list = [
        "Essentials: passport, tickets, wallet",
        "Electronics: phone, charger, power bank",
        "Rain gear: umbrella, waterproof shoes"
    ]
    
    return {
        "destination": destination,
        "weather": weather,
        "hotels": hotels,
        "itinerary": result,
        "budget": budget,
        "packing_list": packing_list
    }

# Save itinerary to JSON in DATA_DIR
def save_itinerary(destination, plan):
    filename = os.path.join(DATA_DIR, f"{destination}_itinerary.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=4)
    print(f"✅ Itinerary saved to {filename}")

# Load itinerary from JSON in DATA_DIR
def load_itinerary(destination):
    filename = os.path.join(DATA_DIR, f"{destination}_itinerary.json")
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        print(f"❌ No saved itinerary found for {destination}.")
        return None

# List available itineraries dynamically
def list_saved_itineraries():
    if not os.path.exists(DATA_DIR):
        return []
    files = [f for f in os.listdir(DATA_DIR) if f.endswith("_itinerary.json")]
    return [os.path.splitext(f)[0].replace("_itinerary", "") for f in files]
