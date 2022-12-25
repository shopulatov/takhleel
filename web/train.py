import requests
import json

API_URL = "https://api-inference.huggingface.co/models/murodbek/uzroberta-sentiment-analysis"
headers = {"Authorization": "Bearer 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"}

def query(comment):
	response = requests.post(API_URL, headers=headers, json=comment)
	return response.json()