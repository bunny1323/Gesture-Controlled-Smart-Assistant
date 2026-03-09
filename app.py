from flask import Flask, request, jsonify
from flask_cors import CORS
from modules.knn_classifier import GestureClassifier
from modules.action_controller import ActionController
from utils.filedb import FileDB
import os

app = Flask(__name__)
@app.route("/")
def home():
    return "Gesture Control Backend Running"
CORS(app)

# Initialize modules
db = FileDB()
classifier = GestureClassifier()
controller = ActionController()

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    # Basic bypass for demo
    return jsonify({"success": True, "user": data['email']})

@app.route('/gestures', methods=['GET'])
def get_gestures():
    gestures = db.load('gestures')
    actions = db.load('actions')
    
    result = []
    for g in gestures:
        result.append({
            "name": g,
            "action": actions.get(g, "None"),
            "active": True
        })
    return jsonify(result)

@app.route('/train_gesture', methods=['POST'])
def train_gesture():
    content = request.json
    name = content.get('name')
    samples = content.get('data') # List of landmark lists
    
    # Store in dataset
    dataset = db.load('dataset')
    for s in samples:
        dataset.append({"name": name, "landmarks": s})
    db.save('dataset', dataset)
    
    # Update gesture list
    gestures = db.load('gestures')
    if name not in gestures:
        gestures.append(name)
        db.save('gestures', gestures)
        
    return jsonify({"success": True})

@app.route('/train_model', methods=['POST'])
def train_model():
    dataset = db.load('dataset')
    if not dataset:
        return jsonify({"error": "No data to train on"}), 400
        
    X = [d['landmarks'] for d in dataset]
    y = [d['name'] for d in dataset]
    
    classifier.train(X, y)
    classifier.load_model() # Force reload into memory
    return jsonify({"success": True})

import time

last_trigger_time = 0
last_action = None
COOLDOWN = 1.5 # 1.5 seconds between different actions

@app.route('/recognize_frame', methods=['POST'])
def recognize_frame():
    global last_trigger_time, last_action
    data = request.json
    landmarks = data.get('landmarks')
    
    if not landmarks:
        return jsonify({"error": "No landmarks"}), 400
        
    gesture, confidence = classifier.predict(landmarks)
    
    if gesture and confidence > 0.7:
        actions = db.load('actions')
        action_key = actions.get(gesture)
        
        if action_key:
            now = time.time()
            # Only trigger if different action or cooldown passed
            if action_key != last_action or (now - last_trigger_time) > COOLDOWN:
                controller.trigger(action_key)
                last_trigger_time = now
                last_action = action_key
                return jsonify({"gesture": gesture, "confidence": float(confidence), "action": action_key, "triggered": True})
            
            return jsonify({"gesture": gesture, "confidence": float(confidence), "action": action_key, "triggered": False})
            
    return jsonify({"gesture": gesture or "None", "confidence": float(confidence)})

@app.route('/map_action', methods=['POST'])
def map_action():
    data = request.json
    gesture = data.get('gesture')
    action = data.get('action')
    
    actions = db.load('actions')
    actions[gesture] = action
    db.save('actions', actions)
    
    return jsonify({"success": True})

if __name__ == '__main__':
    # Ensure folders exist
    os.makedirs('models', exist_ok=True)
    os.makedirs('database', exist_ok=True)
    app.run(host='0.0.0.0', port=5001, debug=True)
