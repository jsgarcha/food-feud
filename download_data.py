import kagglehub
import shutil
import os

path = kagglehub.dataset_download("ahmedshahriarsakib/uber-eats-usa-restaurants-menus", force_download=True)

shutil.copy(path+'/restaurants.csv', './data')
shutil.copy(path+'/restaurant-menus.csv', './data')

print("Downloaded and moved to ./data")