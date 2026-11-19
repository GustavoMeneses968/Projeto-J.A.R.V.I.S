import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()#reza

api_key = os.getenv("GEMINI_API_KEY") #pega a chave da api do .env e coloca na var

print(api_key is not None) #testa se pego a chave da API

client = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=30000, retry_options=types.HttpRetryOptions(attempts=1)))
 #cria o cliente para pode se comunica com o gemini

while True:
    model = "gemini-3.5-flash-lite"
    contents = input()

    try:
        response = client.models.generate_content(model=model, contents=contents)
        
        print(response.text)
    except Exception as erro:
        print(f"Erro: {erro}")
    
