import pandas as pd
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

if "button_rows" not in st.session_state:
    st.session_state.button_rows = []

@st.cache_data
def load_restaurant_data():
    return pd.read_csv('./data/restaurants.csv')

@st.cache_data
def get_random_restaurant(num):
    return df_restaurants.sample(n=num)

def add_prefer(prefer): # Preference is a row in a DataFrame
    st.session_state.prefer.append(prefer) # Build up preferences!
    #st.session_state.not_prefer.remove(prefer) 
    if st.session_state.survey_progress < 100:
        st.session_state.survey_progress += 100//PREFER_NUMBER
        st.session_state.prefer_count -= 1
        survey_progress_bar.progress(st.session_state.survey_progress, text=f"Select {st.session_state.prefer_count} more.")
    
def display_restaurants(df_restaurants):
    restaurants = get_random_restaurant(8) # 8 random restaurants
    st.session_state.not_prefer.append(restaurants) # Assume all not clicked are not preferred; maybe there's a trend
    with col1:
        resturant1 = restaurants.iloc[[0]]
        st.button(resturant1.iloc[0]['name'], use_container_width=True, on_click=add_prefer, args=[resturant1])
        resturant2 = restaurants.iloc[[1]]
        st.button(resturant2.iloc[0]['name'], use_container_width=True, on_click=add_prefer, args=[resturant2])

df_restaurants = load_restaurant_data()

placeholder = st.empty()

if st.session_state.stage == RESTAURANT_SURVEY_STAGE:
    with placeholder.container():
        st.markdown("<h3 style='text-align: center'>Start by taking our survey of eating establishments whose food you enjoy.</h1>", unsafe_allow_html=True)
        survey_progress_bar = st.progress(st.session_state.survey_progress, text=f"Select {st.session_state.prefer_count} more.")
        col1, col2 = st.columns(2) # Fixed 2 columns
        display_restaurants(df_restaurants)
        #if st.button("More restaurants!", type='primary'):

if st.session_state.prefer_count == 0:
    placeholder.empty()
    st.balloons()
    st.session_state.stage = RECIPE_GENERATION_STAGE

if st.session_state.stage == RECIPE_GENERATION_STAGE:
    df_restaurant_preferences = pd.concat(st.session_state.prefer)
    st.dataframe(df_restaurant_preferences)