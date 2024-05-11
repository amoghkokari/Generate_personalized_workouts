import streamlit as st
from PIL import Image

def get_physical_activity_inputs():
    # Get inputs
    activity_image = st.file_uploader("Upload an image of activity/ equipment/ plaace...", type=["jpg", "jpeg", "png"])

    goal = st.text_input('What is your main health goal?', placeholder = "'Lose 5 kg Weight', 'Feel Stronger', 'become lean', 'Have More Energy', 'Feel Better Overall', 'Other'")
    intensity = st.select_slider('How intense do you want your physical activities to be? (1-10)', options=range(1, 11))
    duration = st.text_input('How much time can you dedicate each day? eg. 30 minutes')
    frequency = st.select_slider('How many days a week can you commit', options=[1, 2, 3, 4, 5, 6, 7])

    preferred_activities = st.multiselect('What kinds of physical activities do you enjoy?', ['Sports', 'Hiking', 'Cycling', 'Dancing', 'Gardening', 'Cleaning', 'Other'])
    if 'Other' in preferred_activities:
        custom_input = st.text_input('Please specify other activity:', '')
        if custom_input:
            preferred_activities.append(custom_input)

    any_injuries = st.text_input('Do you have any injuries or health concerns? If yes, please specify')
    in_out = st.selectbox("Preference",["indoor", "outdoor", "both"])
    equipment = st.text_input("Any equipment like dumble, weights or ball you want to use")
    particulars = st.text_input('Do you play or like to start any sports or outdoor activity like tennis, Biking')
    additional_info = st.text_area('Any other information or preferences like 30 days target, you want to share?')

    prompt_enter = st.button("Get Physical Activity Plan")

    activity_image = Image.open(activity_image) if activity_image else ""

    return goal, intensity, duration, frequency, preferred_activities, any_injuries, particulars, additional_info, activity_image, in_out, equipment, prompt_enter