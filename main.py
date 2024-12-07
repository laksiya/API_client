from requests import Response
from flask import Flask, render_template, jsonify
import cv2  # if using OpenCV for camera capture

app = Flask(__name__)

# Route for the main page
@app.route('/')
def home():
    return render_template('index.html')

# API endpoints
@app.route('/api/button1', methods=['POST'])
def button1_action():
    # Add your button 1 logic here
    return jsonify({'message': 'Button 1 action completed'})

@app.route('/api/button2', methods=['POST'])
def button2_action():
    # Add your button 2 logic here
    return jsonify({'message': 'Button 2 action completed'})

@app.route('/api/button3', methods=['POST'])
def button3_action():
    # Add your button 3 logic here
    return jsonify({'message': 'Button 3 action completed'})

@app.route('/api/get-frame')
def get_frame():
    camera_url = f'rtsp://{username}:{password}@{camera_ip}:554/profile2/media.smp'
    # Open the camera stream
    cap = cv2.VideoCapture(camera_url)
    # Capture frame from your camera/source
    ret, frame = cap.read()
    # Convert to jpg
    ret, jpeg = cv2.imencode('.jpg', frame)
    return Response(jpeg.tobytes(), mimetype='image/jpeg')
if __name__ == '__main__':
    app.run(debug=True)
