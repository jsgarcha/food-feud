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
    return pd.read_csv('./data/restaurants.csv')

def add_preferred(): # Preference is a row in a DataFrame
    if st.session_state.progress < 100:
        st.session_state.progress += 100//PREFERRED_NUMBER
        st.session_state.preferred_count -= 1
        progress_bar.progress(st.session_state.progress, text=f"Select {st.session_state.preferred_count} more.")

def display_restaurants(df_restaurants): 
    col1, col2 = st.columns(2) # Fixed 2 columns
    for i in range(4): # Fixed 4 rows
        with col1:
            random_row = df_restaurants.sample()
            st.button(random_row['name'].iloc[0], use_container_width=True, on_click=add_preferred)
        with col2:
            random_row = df_restaurants.sample()
            st.button(random_row['name'].iloc[0], use_container_width=True,  on_click=add_preferred)

df_restaurants = load_restaurant_data()

placeholder = st.empty()

if st.session_state.stage == RESTAURANT_SURVEY_STAGE:
    with placeholder.container():
        st.markdown("<h3 style='text-align: center'>Start by taking our survey of eating establishments whose food you enjoy.</h1>", unsafe_allow_html=True)
        progress_bar = st.progress(st.session_state.progress, text=f"Select {st.session_state.preferred_count} more.")
        display_restaurants(df_restaurants)
        if st.button("More restaurants!", type='primary'):
            display_restaurants(df_restaurants)

if st.session_state.preferred_count == 0:
    placeholder.empty()
    st.balloons()
    st.session_state.stage = RECIPE_GENERATION_STAGE

if st.session_state.stage == RECIPE_GENERATION_STAGE:
    st.write('RECIPE_GENERATION_STAGE')