import kagglehub
import shutil
import os

# Download latest version
path = kagglehub.dataset_download("ahmedshahriarsakib/uber-eats-usa-restaurants-menus", force_download=True)

shutil.move(path+'/restaurants.csv', './data')
shutil.move(path+'/restaurant-menus.csv', './data')

print("Downloaded and moved to ./data/")