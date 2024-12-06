import pandas as pd
import kagglehub
import shutil
import os

# Download data
kaggle_path = kagglehub.dataset_download("ahmedshahriarsakib/uber-eats-usa-restaurants-menus")
data_path = "data/"

print("Downloaded datasets from Kaggle.")

if not os.path.exists(data_path):
    os.makedirs(data_path)

for file in os.listdir(kaggle_path):
    source = os.path.join(kaggle_path, file)
    destination = os.path.join(data_path, file)
    if os.path.isfile(source):
        shutil.copy(source, destination)

print("Moved datasets to data/")

# Load data
restaurants_df = pd.read_csv('data/restaurants.csv') 
print("Loaded data.")

# Clean data
restaurants_df = restaurants_df.dropna(subset=['category']) # Drop rows with null values in 'category'

restaurants_df = restaurants_df[
    (restaurants_df['price_range'].isin(['$$', '$$$', '$$$$'])) &   # Keep $$ to $$$$
    (restaurants_df['score'] >= 3.5)                                # Keep ratings 3.5 and above
]

    # Splitting each entry in category into a single series element
all_categories = (
    restaurants_df['category']
    .str.lower()  # Convert all entries to lowercase
    .str.split(', ')  # Split each entry into a list by ", "
    .explode()  # Flatten the lists into a single series
    .str.strip()  # Remove any leading/trailing whitespace
)

    # Finding the frequencies of each unique category
category_counts = all_categories.value_counts()
sorted_category_counts = category_counts.sort_values(ascending=False)

    # Create an updated dataset
selected_categories = ['steak', 'chinese', 'japanese', 'italian', 'indian', 'mediterranean']

    # Final DataFrame to store the results
final_result = pd.DataFrame()

    # Loop through each category
for category in selected_categories:
    # Filter rows where the category is in the 'categories' column
    filtered = restaurants_df[restaurants_df['category'].str.contains(category, case=False, na=False)]
    
    # Sort by ratings in descending order and select the top 100 entries
    top_entries = filtered.sort_values(by='score', ascending=False).head(100)
    
    # Append the results to the final DataFrame
    final_result = pd.concat([final_result, top_entries])

    # Reset index for the final result
final_result = final_result.reset_index(drop=True)
final_result = final_result.sort_values(by = 'score', ascending=False)

# Export the final dataset to a CSV file
result_file = "top_restaurants.csv"
final_result.to_csv(data_path+result_file, index=False)
print("Cleaned data and exported to "+data_path+result_file)