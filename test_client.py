import requests
from config import config

# Get configuration
base_url = config.get("endpoints.base_url", "http://127.0.0.1:8000")
predict_endpoint = config.get("endpoints.predict_endpoint", "/predict")

# Test single feature prediction
print("=" * 50)
print("Testing POST /predict with single feature")
print("=" * 50)

response = requests.post(
    f"{base_url}{predict_endpoint}",
    json={"feature": 10}
)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

# Test other endpoints
print("\n" + "=" * 50)
print("Testing GET /health")
print("=" * 50)

health_endpoint = config.get("endpoints.health_endpoint", "/health")
response = requests.get(f"{base_url}{health_endpoint}")
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

print("\n" + "=" * 50)
print("Testing GET /")
print("=" * 50)

response = requests.get(f"{base_url}/")
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")

print("\n" + "=" * 50)
print("Testing GET /square?x=5")
print("=" * 50)

response = requests.get(f"{base_url}/square", params={"x": 5})
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
