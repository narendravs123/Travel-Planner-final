import streamlit as st
from langchain_helper import generate_full_travel_plan_with_budget, save_itinerary, load_itinerary, list_saved_itineraries

st.set_page_config(page_title="🌍 AI-Powered Travel Planner", page_icon="✈️")
st.title("🌍 AI-Powered Travel Planner")

# User input
destination = st.text_input("Enter your destination (e.g., Paris, New York, Tokyo)", "Paris")
days = st.number_input("Number of days for your trip", min_value=1, max_value=30, value=3)

if st.button("Generate Itinerary"):
    plan = generate_full_travel_plan_with_budget(destination, days)
    save_itinerary(destination, plan)
    st.success(f"Itinerary for {destination} generated and saved!")
    
    st.header(f"🌍 {destination} Itinerary")
    st.write(f"💸 Budget for {days} days: ${plan['budget']}")
    st.write("🎒 Packing List:", ", ".join(plan['packing_list']))
    st.text("🗓️ Itinerary:")
    st.write(plan['itinerary'])

if st.button("View Saved Itineraries"):
    cities = list_saved_itineraries()
    if cities:
        for city in cities:
            plan = load_itinerary(city)
            if plan:
                st.header(f"🌍 {city}")
                st.write(f"💸 Budget for saved trip: ${plan['budget']}")
                st.write("🎒 Packing List:", ", ".join(plan['packing_list']))
                st.text("🗓️ Itinerary Preview:")
                st.write(plan['itinerary'][:500] + "...")
            else:
                st.warning(f"No saved itinerary found for {city}.")
    else:
        st.warning("No saved itineraries available. Please generate one first!")
