const API_BASE_URL = 'http://localhost:5001';

const api = {
    async post(endpoint, data = {}) {
        try {
            const response = await fetch(`${API_BASE_URL}${endpoint}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });
            return await response.json();
        } catch (error) {
            console.error(`API Error (${endpoint}):`, error);
            return { error: 'Connection failed' };
        }
    },

    async get(endpoint) {
        try {
            const response = await fetch(`${API_BASE_URL}${endpoint}`);
            return await response.json();
        } catch (error) {
            console.error(`API Error (${endpoint}):`, error);
            return { error: 'Connection failed' };
        }
    },

    // Auth
    login: (credentials) => api.post('/login', credentials),
    signup: (userData) => api.post('/signup', userData),

    // Gestures
    getGestures: () => api.get('/gestures'),
    trainGesture: (data) => api.post('/train_gesture', data),
    trainModel: () => api.post('/train_model'),

    // Recognition
    startRecognition: () => api.post('/start_recognition'),
    stopRecognition: () => api.post('/stop_recognition'),
    recognizeFrame: (landmarks) => api.post('/recognize_frame', { landmarks }),

    // Actions
    getActions: () => api.get('/gesture_actions'),
    mapAction: (mapping) => api.post('/map_action', mapping)
};

export default api;
