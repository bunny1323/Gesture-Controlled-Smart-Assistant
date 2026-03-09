import json
import os

class FileDB:
    def __init__(self, base_dir='database'):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)
        
        self.files = {
            'users': 'users.json',
            'gestures': 'gestures.json',
            'dataset': 'gesture_dataset.json',
            'actions': 'gesture_actions.json'
        }
        
        # Initialize empty files if they don't exist
        for key, name in self.files.items():
            path = os.path.join(self.base_dir, name)
            if not os.path.exists(path):
                with open(path, 'w') as f:
                    content = {} if key == 'actions' else []
                    json.dump(content, f)

    def _get_path(self, key):
        return os.path.join(self.base_dir, self.files[key])

    def load(self, key):
        with open(self._get_path(key), 'r') as f:
            return json.load(f)

    def save(self, key, data):
        with open(self._get_path(key), 'w') as f:
            json.dump(data, f, indent=4)

    def append(self, key, item):
        data = self.load(key)
        data.append(item)
        self.save(key, data)
