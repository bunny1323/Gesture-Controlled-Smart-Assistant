import requests
import json
import os

BASE_URL = "http://localhost:5001"

def seed_data():
    print("--- Seeding Standard Gestures ---")
    
    # Simple landmarks for "Palm" (all fingers up)
    palm_landmarks = [{"x": 0.5, "y": 0.5 - (0.05 * i), "z": 0.0} for i in range(21)]
    # Simple landmarks for "Fist" (all fingers down/bunched)
    fist_landmarks = [{"x": 0.5, "y": 0.5 + (0.01 * i), "z": 0.0} for i in range(21)]
    
    # 1. Train Palm
    requests.post(f"{BASE_URL}/train_gesture", json={
        "name": "Open Palm",
        "data": [palm_landmarks] * 20
    })
    
    # 2. Train Fist
    requests.post(f"{BASE_URL}/train_gesture", json={
        "name": "Fist",
        "data": [fist_landmarks] * 20
    })
    
    # 3. Map Actions
    requests.post(f"{BASE_URL}/map_action", json={"gesture": "Open Palm", "action": "play_pause"})
    requests.post(f"{BASE_URL}/map_action", json={"gesture": "Fist", "action": "stop_engine"})
    
    # 4. Train Model
    requests.post(f"{BASE_URL}/train_model")
    print("Seeding complete and model retrained.")

if __name__ == "__main__":
    seed_data()
