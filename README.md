# Food Feud
## How to run locally
Python 3 and git are required.
1) `https://github.com/jsgarcha/food-feud`
2) `cd ./food-feud`
3) `pip install -r requirements.txt`
4) `python clean_data.py`
5) `streamlit run main.py`

Running the first time may take a minute or so, depending on your internet connection, because the model from Huggingface (~900mb) has to be downloaded.
Subsequent executions will not pause for long since the model will already be in cache. 

You also need to provide your own key to 