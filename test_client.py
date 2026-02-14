import requests

response = requests.post("http://127.0.0.1:8000/predict", json={"feature": 10 })

print(response.json())
