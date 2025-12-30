import time
import random

def make_api_request():
    if random.random() < 0.8:
        raise Exception("Network glitch!")
    return "Success!"

attempts = 0
while attempts < 3:
    try:
        response = make_api_request()
        print("API request succeeded:", response)
        break
    except Exception as e:
        print("API request failed:", e)
        attempts += 1
        time.sleep(1)