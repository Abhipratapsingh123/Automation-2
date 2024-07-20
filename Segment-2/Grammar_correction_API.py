import requests
import json

url = "https://api.languagetool.org/v2/check"
data = {
  'text':'I has an apple',
  'language':'auto'
}

response = requests.post(url,data = data)
result = json.loads(response.text)
print(result['matches'][1]['replacements'][0])

