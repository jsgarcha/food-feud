# Imports
import pandas as pd
import random
from sklearn.model_selection import train_test_split

# Load the datasets
df_restaurants = pd.read_csv('data/restaurants.csv')
df_menus = pd.read_csv('data/restaurant-menus.csv')

asked_restaurants = set()
preferred_restaurants = []
preference_number = 20

# Loops until it finds a restaurant that wasn't asked about before
def get_restaurant():
    while True:
        restaurant = random.choice(df_restaurants['name'])
        if restaurant not in asked_restaurants:
            asked_restaurants.add(restaurant)
            return restaurant

#Check if user prefers restaurant ("Do you like X?") If so, add to preference. If not, ask again.
while len(preferred_restaurants) <= preference_number:
    restaurant = get_restaurant()
    prefers = input('Do you like ' + restaurant + '? (y/n)')
    if prefers == 'y':
        preferred_restaurants.append(restaurant)