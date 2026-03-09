import api from './api.js';

const App = {
    init() {
        console.log("Vision Assistant Initialized");
        this.setupEventListeners();
        this.updateActiveNavLink();
        this.checkAuth();
    },

    setupEventListeners() {
        // Global event listeners
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', (e) => {
                // Handling nav clicks if needed
            });
        });

        // Logout listener if element exists
        const logoutBtn = document.getElementById('logout-btn');
        if (logoutBtn) {
            logoutBtn.addEventListener('click', () => this.logout());
        }
    },

    updateActiveNavLink() {
        const path = window.location.pathname;
        const page = path.split('/').pop();
        document.querySelectorAll('.nav-link').forEach(link => {
            if (link.getAttribute('href') === page) {
                link.classList.add('active');
            } else {
                link.classList.remove('active');
            }
        });
    },

    async checkAuth() {
        // Simplified auth check - in production would verify token
        const user = localStorage.getItem('user');
        const isAuthPage = ['index.html', 'signup.html'].some(p => window.location.pathname.includes(p));

        if (!user && !isAuthPage) {
            window.location.href = 'index.html';
        } else if (user && isAuthPage) {
            window.location.href = 'dashboard.html';
        }
    },

    logout() {
        localStorage.removeItem('user');
        window.location.href = 'index.html';
    },

    log(message, type = 'info') {
        const console = document.getElementById('log-console');
        if (console) {
            const entry = document.createElement('div');
            entry.className = `log-entry ${type}`;
            const time = new Date().toLocaleTimeString();
            entry.textContent = `[${time}] ${message}`;
            console.prepend(entry);
        }
    }
};

document.addEventListener('DOMContentLoaded', () => App.init());

export default App;
