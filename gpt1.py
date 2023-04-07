import os
import openai
import json
import requests
from dotenv import load_dotenv

load_dotenv()

test = os.getenv("OPENAI_API_KEY")

# print(os.environ)

# Define the API endpoint URL
url = "https://api.openai.com/v1/chat/completions"

# Set the OpenAI API key
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + test
}

# Define the payload data
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.7
}

# Convert the payload to a JSON string
json_payload = json.dumps(payload)

# Send the POST request to the API endpoint
response = requests.post(url, headers=headers, data=json_payload)

# Extract the response data
response_data = response.json()

# Print the response
print(response_data)
