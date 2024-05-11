import streamlit as st
from datetime import datetime, timezone
from firebase_admin import firestore, credentials, initialize_app, _apps

if not _apps:
    cred = credentials.Certificate(dict(st.secrets['profile']))
    initialize_app(cred)

def build_user_input(goal, intensity, duration, frequency, preferred_activities, any_injuries, particulars, additional_info, activity_image, in_out, equipment):
    dct_inputs = {
        "goal": goal,
        "intensity": intensity,
        "duration": duration,
        "frequency": frequency,
        "preferred_activities": preferred_activities,
        "any_injuries": any_injuries,
        "particulars": particulars,
        "additional_info": additional_info,
        "activity_image": activity_image,
        "in_out": in_out,
        "equipment": equipment
    }
    return dct_inputs

def store_to_db(collection, values):
    try:
        db = firestore.client()
        gmt_time = datetime.now(timezone.utc)
        document_id = "workout_v1_"+str(gmt_time)
        # Store the feedback data in Firestore
        new_doc = db.collection(collection).document(document_id)
        new_doc.set(values)
        return True
    
    except Exception as error1:
        st.write("Please check your Api key, probable issue", SystemExit(error1))
        return False

@st.experimental_fragment
def get_feedback(user_inputs, resp):
    rating = st.select_slider(label="likeness", options=["😞","🙁","😐","🙂","😀"], key='rating', label_visibility='hidden')
    feedback = st.text_area(label="Feedback", placeholder=" I like the application, gave good response but I would love to see .....")

    score_mappings = {
        "thumbs": {"👍": 1, "👎": 0},
        "faces": {"😀": 5, "🙂": 4, "😐": 3, "🙁": 2, "😞": 1},
    }

    enter_feedback = st.button("Save Feedback")

    if enter_feedback:
        feedback_data = {
            "response": resp,
            "prompt_inputs": user_inputs,
            "feedback": feedback,
            "rating": score_mappings["faces"][rating]
        }
        store_to_db("feedback" ,feedback_data)
    
        st.write("Thank you for your valuable feedback, dont forget to follow on [Github](https://github.com/amoghkokari) !!")

    return