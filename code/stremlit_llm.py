# Bring in deps
import streamlit as st
from prompts import build_prompt
import google.generativeai as genai
from get_inputs import get_physical_activity_inputs
from feedback import build_user_input, get_feedback

def main():
    # App framework
    st.title('🤾‍♀️💪🏋️🤸 Get My Excercise Routine')
    st.subheader('Get Weekly Exercise routine based on Goal and target, Time Required, Cuisines and Equipment available (all inputs are optional)')

    api_key =  st.text_input('Enter Google Generative AI API KEY (Required)')
    st.link_button("Click for API KEY (select create api key in new project)", "https://makersuite.google.com/app/apikey", type="secondary")

    goal, intensity, duration, frequency, preferred_activities, any_injuries, particulars, additional_info, activity_image, in_out, equipment, prompt_enter = get_physical_activity_inputs()
    prompt = build_prompt(goal, intensity, duration, frequency, preferred_activities, any_injuries, particulars, additional_info, activity_image, in_out, equipment)

    # Llms
    llm_api_key = api_key if api_key else st.secrets["api_key"]
    genai.configure(api_key=llm_api_key)
    model = genai.GenerativeModel(model_name = "gemini-pro")

    st.write("Made with ❤️ by Amogh Mahadev kokari ©️ 2024 _||_ [linkedin](https://www.linkedin.com/in/amoghkokari/) _||_ [Portfolio](https://amoghkokari.github.io/portfolio.pdf) _||_ [Github](https://github.com/amoghkokari)")

    # Show stuff to the screen if there's a prompt
    try:
        if prompt_enter:
            response = model.generate_content(prompt)
            st.write(response.text)
            u_inputs = build_user_input(goal, intensity, duration, frequency, preferred_activities, any_injuries, particulars, additional_info, activity_image, in_out, equipment)
            get_feedback(u_inputs, response.text)            

    except Exception as error:
        st.write("Please check your Api key, probable issue", SystemExit(error))

if __name__ == "__main__":
    main()