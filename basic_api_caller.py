import requests
import json
from  api_keys import key
# Your API key
api_key = "YOUR_API_KEY_HERE"

# The API endpoint
url = "https://api.anthropic.com/v1/messages"

# The query you want to send
query = "What is the capital of France?"

# Headers for the request
headers = {
    "Content-Type": "application/json",
    "X-API-Key": api_key,
}

# The data payload
data = {
    "model": "claude-2",  # or whichever model version you're using
    "messages": [
        {
            "role": "user",
            "content": query
        }
    ],
    "max_tokens_to_sample": 300
}

# Send the POST request
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    result = response.json()
    
    # Extract and print the assistant's reply
    assistant_reply = result['content'][0]['text']
    print("Claude's response:", assistant_reply)
else:
    print("Error:", response.status_code, response.text)
