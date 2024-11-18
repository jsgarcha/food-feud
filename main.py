import pandas as pd
import random
import streamlit as st

st.markdown("<h1 style='text-align: center'><a href='https://github.com/jsgarcha/food-feud'>Food Feud</a></h1>", unsafe_allow_html=True)

RESTAURANT_SURVEY_STAGE = 1
RECIPE_GENERATION_STAGE = 2

PREFERRED_NUMBER = 20

if 'stage' not in st.session_state:
    st.session_state.stage = RESTAURANT_SURVEY_STAGE # Start stage

if "preferred" not in st.session_state:
    st.session_state.preferred = []

if "not_preferred" not in st.session_state:
    st.session_state.not_preferred = []

if "preferred_count" not in st.session_state:
    st.session_state.preferred_count = PREFERRED_NUMBER

if "progress" not in st.session_state:
    st.session_state.progress = 0

@st.cache_data
def load_restaurant_data():
    df_restaurants = pd.read_csv('./data/restaurants.csv')
    return df_restaurants

def add_preferred():
    if st.session_state.progress < 100:
        st.session_state.progress += 100//PREFERRED_NUMBER
        st.session_state.preferred_count -= 1
        progress_bar.progress(st.session_state.progress, text=f"Select {st.session_state.preferred_count} more.")

def display_restaurants(df_restaurants): 
    col1, col2 = st.columns(2) # Fixed 2 columns
    for i in range(4): # Fixed 4 Rows
        with col1:
            row = df_restaurants.sample()
            name = row['name']
            st.button(str(name), use_container_width=True, on_click=add_preferred)

df_restaurants = load_restaurant_data()

if st.session_state.stage == RESTAURANT_SURVEY_STAGE:
    st.markdown("<h3 style='text-align: center'>Start by taking our survey of eating establishments whose food you enjoy.</h1>", unsafe_allow_html=True)
    progress_bar = st.progress(st.session_state.progress, text=f"Select {st.session_state.preferred_count} more.")
    display_restaurants(df_restaurants)
    if st.button("More restaurants!", type='primary'):
        display_restaurants(df_restaurants)

if st.session_state.preferred_count == 0:
    st.session_state.stage = RECIPE_GENERATION_STAGE

if st.session_state.stage == RECIPE_GENERATION_STAGE:
    progress_bar.empty()
    st.balloons()