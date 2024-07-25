import requests
import json

url = "https://api.languagetool.org/v2/check"
data = {
    'text': 'I has an  Tree',
    'language': 'auto'
}

response = requests.post(url, data=data)
result = json.loads(response.text)

# Check if there are matches in the result
if 'matches' in result and len(result['matches']) > 0:
    # Iterate through matches to find replacements
    for match in result['matches']:
        if 'replacements' in match and len(match['replacements']) > 0:
            print(match['replacements'][0]['value'])
else:
    print("No matches or replacements found.")
