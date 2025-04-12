import json
import requests

# Load the configuration from the JSON file
with open('run_settings.json', 'r') as file:
run_settings = json.load(file)

# Example function to make a request to the AI model
def generate_response(prompt):
url = "https://api.your-ai-service.com/generate"
headers = {
"Content-Type": "application/json",
"Authorization": "AIzaSyAvrxOyAVzPVcnzxuD0mjKVDyS2bNWfC10"
}
payload = {
"prompt": prompt,
"temperature": run_settings["temperature"],
"endTokens": run_settings["endTokens"],
"model": run_settings["model"],
"candidateCount": run_settings["candidateCount"],
"topP": run_settings["topP"],
"topK": run_settings["topK"],
"maxOutputTokens": run_settings["maxOutputTokens"],
"safetySettings": run_settings["safetySettings"],
"responseMimeType": run_settings["responseMimeType"]
}

response = requests.post(url, headers=headers, json=payload)
return response.json()

# Example usage
prompt = "Tell me a story about a brave knight."
response = generate_response(prompt)
print(response)
