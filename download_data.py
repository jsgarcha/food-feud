import kagglehub
import shutil
import os

kaggle_path = kagglehub.dataset_download("ahmedshahriarsakib/uber-eats-usa-restaurants-menus", force_download=True)

data_path = "./data"
if not os.path.exists(data_path):
    os.makedirs(data_path)

shutil.copy(kaggle_path+'/restaurants.csv', './data')
shutil.copy(kaggle_path+'/restaurant-menus.csv', './data')

print("Downloaded and moved to ./data")