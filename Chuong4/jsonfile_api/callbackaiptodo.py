import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
todos = response.json()
print(todos[0])
for t in todos[:2]:
    jsonObj = json.dumps(t, ensure_ascii=False, indent=3)
    print(jsonObj)

