import pandas as pd
import streamlit as st
import json
from recipe_generator import generation_function
from gemini import chat_session

st.markdown("<h1 style='text-align: center'>Food Feud</h1>", unsafe_allow_html=True)

RESTAURANT_SURVEY_STAGE = 1
RECIPE_GENERATION_STAGE = 2

LIKE_NUMBER = 20

if 'stage' not in st.session_state:
    st.session_state.stage = RESTAURANT_SURVEY_STAGE # Start stage

if "like" not in st.session_state:
    st.session_state.like = []

if "dislike" not in st.session_state:
    st.session_state.dislike = []

if "like_count" not in st.session_state:
    st.session_state.like_count = LIKE_NUMBER

if "survey_progress" not in st.session_state:
    st.session_state.survey_progress = 0

data_path = "data/"
data_file = "top_restaurants.csv"

@st.cache_data
def load_restaurant_data():
    return pd.read_csv(data_path+data_file)

def add_like(like): # Row in a DataFrame
    st.session_state.like.append(like) # Build up likes
    if st.session_state.survey_progress < 100:
        st.session_state.survey_progress += 100//LIKE_NUMBER
        st.session_state.like_count -= 1
        survey_progress_bar.progress(st.session_state.survey_progress, text=f"Select {st.session_state.like_count} more.")

def add_dislike(dislike):
     st.session_state.dislike.append(dislike)

ingredients = ['chicken']

def generate_recipe(ingredients):
    generated = generation_function(ingredients)
    for text in generated:
        sections = text.split("\n")
        for section in sections:
            section = section.strip()
            if section.startswith("title:"):
                section = section.replace("title:", "")
                headline = "TITLE"
            elif section.startswith("ingredients:"):
                section = section.replace("ingredients:", "")
                headline = "Ingredients"
            elif section.startswith("directions:"):
                section = section.replace("directions:", "")
                headline = "Directions"
            
            if headline == "TITLE":
                st.markdown("<h3 style='text-align: center'>"+str(section.strip().capitalize())+"</h3>", unsafe_allow_html=True)
            else:
                section_info = [f"  - {info.strip().capitalize()}" for i, info in enumerate(section.split("--"))]
                st.markdown("<h4>"+f'{headline}'+"</h4>", unsafe_allow_html=True)
                st.write("\n".join(section_info))

df_restaurants = load_restaurant_data()

placeholder = st.empty()

if st.session_state.stage == RESTAURANT_SURVEY_STAGE:
    with placeholder.container():
        st.markdown("<h4 style='text-align: center'>Start by taking our survey of eating establishments whose food you enjoy.</h4>", unsafe_allow_html=True)
        survey_progress_bar = st.progress(st.session_state.survey_progress, text=f"Select {st.session_state.like_count} more.")
        restaurant = df_restaurants.sample()
        st.markdown("<h3 style='text-align: center'>"+restaurant.iloc[0]['name']+"</h3>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        if col1.button('Yes 👍', type="secondary", use_container_width=True):
            add_like(restaurant)
        if col2.button('No 👎', type="secondary", use_container_width=True):
            add_dislike(restaurant)

if st.session_state.like_count == 0 and st.session_state.stage != RECIPE_GENERATION_STAGE:
    placeholder.empty()
    st.balloons()
    st.session_state.stage = RECIPE_GENERATION_STAGE

if st.session_state.stage == RECIPE_GENERATION_STAGE:
    df_restaurant_likes = pd.concat(st.session_state.like)
    
    if st.button('Generate Recipe!', type='primary'):
        response = chat_session.send_message("")
        model_response = response.text
        response = json.loads(model_response)
        st.write(response)
        
        #generate_recipe(ingredients)
