import streamlit as st
from main import generate_response

st.title("😋Meal buddy")

st.write("A assitant that help to make your scheudle.")

human_input = st.text_input("Which allergies do you have, what ingredients do you currently have, and for how many days do you want your schedule?")

if human_input:
    answer = generate_response(human_input)
    st.write(answer)