import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config={"temperature": 2,"top_p": 0.95,"top_k": 40,"max_output_tokens": 8192,"response_mime_type": "application/json"})
chat_session = model.start_chat()