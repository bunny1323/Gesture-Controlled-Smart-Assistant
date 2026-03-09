class WebcamHandler {
    constructor(videoElementId, canvasElementId) {
        this.video = document.getElementById(videoElementId);
        this.canvas = document.getElementById(canvasElementId);
        if (this.canvas) {
            this.ctx = this.canvas.getContext('2d');
        }
        this.stream = null;
        this.isActive = false;
    }

    async start() {
        try {
            this.stream = await navigator.mediaDevices.getUserMedia({
                video: { width: 1280, height: 720 }
            });
            this.video.srcObject = this.stream;
            this.isActive = true;
            return true;
        } catch (err) {
            console.error("Error accessing webcam:", err);
            return false;
        }
    }

    stop() {
        if (this.stream) {
            this.stream.getTracks().forEach(track => track.stop());
            this.video.srcObject = null;
            this.isActive = false;
        }
    }

    drawSkeleton(landmarks) {
        if (!this.ctx || !landmarks) return;

        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        // Generic MediaPipe style drawing
        this.ctx.fillStyle = "#0070f3";
        this.ctx.strokeStyle = "white";
        this.ctx.lineWidth = 2;

        landmarks.forEach(point => {
            const x = point.x * this.canvas.width;
            const y = point.y * this.canvas.height;
            this.ctx.beginPath();
            this.ctx.arc(x, y, 4, 0, Math.PI * 2);
            this.ctx.fill();
        });

        // Add connections (simplified)
        const connections = [
            [0, 1, 2, 3, 4], [0, 5, 6, 7, 8], [5, 9], [9, 10, 11, 12],
            [9, 13], [13, 14, 15, 16], [13, 17], [17, 18, 19, 20], [0, 17]
        ];

        this.ctx.beginPath();
        connections.forEach(path => {
            this.ctx.moveTo(landmarks[path[0]].x * this.canvas.width, landmarks[path[0]].y * this.canvas.height);
            for (let i = 1; i < path.length; i++) {
                this.ctx.lineTo(landmarks[path[i]].x * this.canvas.width, landmarks[path[i]].y * this.canvas.height);
            }
        });
        this.ctx.stroke();
    }

    captureFrame() {
        const offscreen = document.createElement('canvas');
        offscreen.width = this.video.videoWidth;
        offscreen.height = this.video.videoHeight;
        offscreen.getContext('2d').drawImage(this.video, 0, 0);
        return offscreen.toDataURL('image/jpeg');
    }
}

export default WebcamHandler;
