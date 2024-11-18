import pandas as pd
import random
import streamlit as st

st.markdown(
    "<h1 style='text-align: center'><a href='https://github.com/jsgarcha/food-feud'>Food Feud</a></h1>"
    "<h3 style='text-align: center'>Start by taking our survey of eating establishments whose food you enjoy.</h1>",
    unsafe_allow_html=True
)

PREFERRED_NUMBER = 20
not_preferred = []
preferred = []

if "progress" not in st.session_state:
    st.session_state.progress = 0

if "preferred_count" not in st.session_state:
    st.session_state.preferred_count = PREFERRED_NUMBER

if "button_key" not in st.session_state:
    st.session_state.button_key = 1

@st.cache_data
def load_restaurant_data():
    df_restaurants = pd.load_csv('./data/restaurants.csv')
    return df_restaurants

def add_preferred():
    if st.session_state.progress < 100:
        st.session_state.progress += 100//PREFERRED_NUMBER  # Increment progress by 10
        st.session_state.preferred_count -= 1
        progress_bar.progress(st.session_state.progress, text=f"Select {st.session_state.preferred_count} more.")

def survey_results():
    return 0

progress_bar = st.progress(st.session_state.progress, text=f"Select {st.session_state.preferred_count} more.")

col1, col2 = st.columns(2)

for i in range(4):
    with col1:
        st.button(str(st.session_state.button_key), key=st.session_state.button_key, use_container_width=True)
        st.session_state.button_key += 1
    with col2:
        st.button(str(st.session_state.button_key), key=st.session_state.button_key, use_container_width=True)
        st.session_state.button_key += 1

# "Load More" button logic
if st.button("More restaurants!", key=0):
    st.session_state.current_page += 1

if st.session_state.preferred_count == 0:
    progress_bar.empty()
    st.balloons()
    survey_results()