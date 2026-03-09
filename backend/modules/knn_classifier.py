import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pickle
import os

class GestureClassifier:
    def __init__(self, model_path='models/gesture_knn_model.pkl'):
        self.model_path = model_path
        self.model = None
        self.label_map = []
        
        if os.path.exists(self.model_path):
            try:
                self.load_model()
            except:
                print("Model file corrupted or incompatible. Training required.")

    def preprocess_landmarks(self, landmarks):
        """
        Convert 21 landmarks (x, y, z) into a flat feature vector.
        Normalizes relative to the wrist (landmark 0) and scales by 
        the distance to the middle finger base (landmark 9).
        """
        coords = np.array([[lm['x'], lm['y'], lm['z']] for lm in landmarks])
        wrist = coords[0]
        
        # Relative coordinates
        relative_coords = coords - wrist
        
        # Scale by distance between wrist (0) and middle finger MCP (9)
        # This makes it invariant to hand-to-camera distance
        palm_size = np.linalg.norm(relative_coords[9])
        if palm_size > 0:
            relative_coords /= palm_size
            
        return relative_coords.flatten()

    def train(self, data_list, labels):
        """
        data_list: List of raw landmark lists
        labels: List of string names for each data point
        """
        X = [self.preprocess_landmarks(d) for d in data_list]
        unique_labels = sorted(list(set(labels)))
        y = [unique_labels.index(l) for l in labels]
        
        self.label_map = unique_labels
        self.model = KNeighborsClassifier(n_neighbors=3)
        self.model.fit(X, y)
        
        self.save_model()
        return True

    def predict(self, landmarks):
        if self.model is None:
            return None, 0.0
            
        feat = self.preprocess_landmarks(landmarks).reshape(1, -1)
        probs = self.model.predict_proba(feat)[0]
        idx = np.argmax(probs)
        confidence = probs[idx]
        
        return self.label_map[idx], confidence

    def save_model(self):
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        with open(self.model_path, 'wb') as f:
            pickle.dump({'model': self.model, 'labels': self.label_map}, f)

    def load_model(self):
        with open(self.model_path, 'rb') as f:
            data = pickle.load(f)
            self.model = data['model']
            self.label_map = data['labels']
