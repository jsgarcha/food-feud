import pandas as pd
import numpy as np
import random

df_restaurants = pd.read_csv('data/restaurants.csv')
df_restaurant_menus = pd.read_csv('data/restaurant-menus.csv')

user_preferences = []
while len(user_preferences) <= 10:
    random.choice(df_restaurants['id'])
    restaurant_name = df_restaurants[]
    print('Do you like {}')