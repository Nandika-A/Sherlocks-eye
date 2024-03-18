import requests
from dotenv import dotenv_values

env_vars = dotenv_values(".env")
API_URL = "https://api-inference.huggingface.co/models/arpanghoshal/EmoRoBERTa"
headers = {"Authorization": "Bearer " + env_vars["API_TOKEN"]}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "I like you. I love you",
})
first = output[0][0]
print(first)