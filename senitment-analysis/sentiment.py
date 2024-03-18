import requests

API_URL = "https://api-inference.huggingface.co/models/arpanghoshal/EmoRoBERTa"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "I like you. I love you",
})
first = output[0][0]
print(first)