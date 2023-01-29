import mediapipe as mp
import numpy as np
import streamlit as st 
import main
from PIL import Image
import requests
from streamlit_lottie import st_lottie
from annotated_text import annotated_text

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
website_icon = Image.open('FitGenie.jpg')   

st.set_page_config(
    page_title='FitGenie',
    page_icon=website_icon
    )

st.sidebar.markdown("""# <u>Exercises:</u>""",unsafe_allow_html=True)
st.sidebar.markdown(""" #  Biceps
    ##### For <u>biceps</u>, please place your <i>arms</i> and the left side of your body in _full view_ of the camera!
    #  Squats 
    ##### For <u>squats</u>, please place your <i>legs</i> and <i>feet</i> in _full view_ of the camera!
    #  Crunches 
    ##### For <u>crunches</u>, please <i>lay</i> down and keep the <i>left side</i> of your entire body in _full view_ of the camera!
    #  Bench Press 
    ##### For <u>bench press</u>, please <i>lay</i> down and keep the <i>left side</i> of your body in _full view_ of the camera!
""",unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    st.title("FitGenie")
    st.write("Select an exercise:")

    biceps = st.checkbox('Biceps')
    squats = st.checkbox('Squats')
    crunches = st.checkbox('Crunches')
    benchpress = st.checkbox('BenchPress')

    exercise_list = [biceps, squats, crunches, benchpress]
    exercises = ['Biceps', 'Squats','Crunches','BenchPress']
    exercise_to_do = {}

    for count, item in enumerate(exercise_list):
        if item:
            selected = True 
            user_input_rep = st.text_input("Please enter rep amount: " + exercises[count], key=f"rep_{count}")
            user_input_sets = st.text_input("Please enter set amount: " + exercises[count],key=f"sets_{count}")
            exercise_to_do[exercises[count]] = {"reps":user_input_rep,"sets":user_input_sets}
    options = st.button("Click me to begin.")
    if options:
        st.write(exercise_to_do)
        main.start(exercise_to_do)

with col2:
    lottie_url = 'https://assets5.lottiefiles.com/packages/lf20_V9t630.json'
    lottie_json = load_lottieurl(lottie_url)
    st_lottie(lottie_json, key='diagram')
    annotated_text(
        "Hello there! I'm FitGenie, your personal fitness assistant.",
    )