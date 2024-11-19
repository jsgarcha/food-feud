import pandas as pd
import random
import streamlit as st

st.markdown("<h1 style='text-align: center'><a href='https://github.com/jsgarcha/food-feud'>Food Feud</a></h1>", unsafe_allow_html=True)

RESTAURANT_SURVEY_STAGE = 1
RECIPE_GENERATION_STAGE = 2

PREFER_NUMBER = 20

if 'stage' not in st.session_state:
    st.session_state.stage = RESTAURANT_SURVEY_STAGE # Start stage

if "prefer" not in st.session_state:
    st.session_state.prefer = []

if "not_prefer" not in st.session_state:
    st.session_state.not_prefer = []

if "prefer_count" not in st.session_state:
    st.session_state.prefer_count = PREFER_NUMBER

if "survey_progress" not in st.session_state:
    st.session_state.survey_progress = 0

@st.cache_data
def load_restaurant_data():
    return pd.read_csv('./data/restaurants.csv')

def add_prefer(prefer): # Preference is a row in a DataFrame
    st.session_state.prefer.append(prefer) # Build up preferences!
    #st.session_state.not_prefer.remove(prefer)
    if st.session_state.survey_progress < 100:
        st.session_state.survey_progress += 100//PREFER_NUMBER
        st.session_state.prefer_count -= 1
        survey_progress_bar.progress(st.session_state.survey_progress, text=f"Select {st.session_state.prefer_count} more.")
    

def display_restaurants(df_restaurants): 
    col1, col2 = st.columns(2) # Fixed 2 columns
    for i in range(4): # Fixed 4 rows
        with col1:
            random_row = df_restaurants.sample()
            df_restaurants.drop(random_row.index, axis=0, inplace=True) # Remove sample from original, so isn't sampled twice (or more)
            st.session_state.not_prefer.append(random_row) # Assume all not-clicked are not-prefers; maybe there's a trend to eventually see
            st.button(random_row['name'].iloc[0], use_container_width=True, on_click=add_prefer, args=[random_row])

df_restaurants = load_restaurant_data()

placeholder = st.empty()

if st.session_state.stage == RESTAURANT_SURVEY_STAGE:
    with placeholder.container():
        st.markdown("<h3 style='text-align: center'>Start by taking our survey of eating establishments whose food you enjoy.</h1>", unsafe_allow_html=True)
        survey_progress_bar = st.progress(st.session_state.survey_progress, text=f"Select {st.session_state.prefer_count} more.")
        display_restaurants(df_restaurants)
        if st.button("More restaurants!", type='primary'):
            display_restaurants(df_restaurants)

if st.session_state.prefer_count == 0:
    placeholder.empty()
    st.balloons()
    st.session_state.stage = RECIPE_GENERATION_STAGE

if st.session_state.stage == RECIPE_GENERATION_STAGE:
    df_restaurant_preferences = pd.concat(st.session_state.prefer)
    st.dataframe(df_restaurant_preferences)