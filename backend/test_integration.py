import requests
import time

BASE_URL = "http://localhost:5001"

def test_backend():
    print("--- Testing Backend API ---")
    
    # 1. Test Login
    try:
        res = requests.post(f"{BASE_URL}/login", json={"email": "test@example.com", "password": "password"})
        print(f"Login Response: {res.json()}")
    except Exception as e:
        print(f"Login failed: {e}")
        return

    # 2. Test Getting Gestures
    res = requests.get(f"{BASE_URL}/gestures")
    print(f"Gestures: {res.json()}")

    # 3. Test Training a Mock Gesture
    mock_landmarks = [{"x": 0.1 * i, "y": 0.2 * i, "z": 0.01 * i} for i in range(21)]
    res = requests.post(f"{BASE_URL}/train_gesture", json={
        "name": "test_gesture",
        "data": [mock_landmarks] * 10
    })
    print(f"Train Gesture: {res.json()}")

    # 4. Train Model
    res = requests.post(f"{BASE_URL}/train_model")
    print(f"Train Model: {res.json()}")

    # 5. Map Action
    res = requests.post(f"{BASE_URL}/map_action", json={
        "gesture": "test_gesture",
        "action": "scroll_down"
    })
    print(f"Map Action: {res.json()}")

    # 6. Test Recognition (Should trigger scroll)
    print("Testing recognition (look for 'Executing System Action' in server logs)...")
    res = requests.post(f"{BASE_URL}/recognize_frame", json={
        "landmarks": mock_landmarks
    })
    print(f"Recognition Result: {res.json()}")

if __name__ == "__main__":
    test_backend()
