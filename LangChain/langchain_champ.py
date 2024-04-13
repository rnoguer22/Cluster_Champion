import os
from dotenv import load_dotenv
from langchain_openai import OpenAI



load_dotenv()

OPENAI_API_KEY = str(input('Enter your OpenAI API Key: '))

llm = OpenAI(openai_api_key = OPENAI_API_KEY)
result = llm.invoke('Dime los ganadores de las pasadas 4 UEFA Champions League')
print(result)   