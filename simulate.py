import requests
import random
import time

while True:
    data = {
        "tag": "tiger-001",
        "name": "Tiger",
        "location": [random.uniform(10, 11), random.uniform(76, 77)],
        "heart_rate": random.randint(60, 100),
        "temperature": round(random.uniform(36.5, 39.0), 1)
    }
    try:
        res = requests.post("http://localhost:5000/update", json=data)
        print(res.json())
    except:
        print("Server not running.")
    time.sleep(5)
