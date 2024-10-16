import pandas as pd
import numpy as np
import random

df_restaurants = pd.read_csv('data/restaurants.csv')
df_restaurant_menus = pd.read_csv('data/restaurant-menus.csv')

print(random.choice(df_restaurants['name']))

# Maybe ask for 2 things: 'category' and 'price' rather than random?

#user_preferences = []
#while len(user_preferences) <= 10:
#    random.choice(df_restaurants['id'])
#    restaurant_name = df_restaurants[]
#    print('Do you like {}')

# Currently, assume one user.
# Train model on user_preferences. 
# Then check with user, "was this to your liking?" If not, ask for preferences again and re-train.