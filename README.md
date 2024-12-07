# Food Feud
## How to run locally
Python 3 and git are required.
1) `https://github.com/jsgarcha/food-feud`
2) `cd ./food-feud`
3) `pip install -r requirements.txt`
4) `python clean_data.py`
5) `streamlit run main.py`

NOTE: JAX v0.4.36 does not work for this Huggingface model (https://huggingface.co/flax-community/t5-recipe-generation)
`pip install --force-reinstall -v "jax==0.4.34"`

Running the first time may take a minute or so, depending on your internet connection, because the model has to be downloaded from Huggingface (~900mb) .
Subsequent executions will not pause for long since the model will already be in cache. 

You also need to provide your own key for Gemini in `.env` under the `GEMINI_API_KEY` key.