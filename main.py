from requests import Response
from flask import Flask, render_template, jsonify
from credentials import DEMO_KEY
app = Flask(__name__)

# Route for the main page
@app.route('/')
def home():
    return render_template('index.html')

# API endpoints
@app.route('/api/get-time', methods=['POST'])
def get_time():
    from datetime import datetime
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({'message': f'Current time is: {current_time}'})

@app.route('/api/nasa-image', methods=['POST'])
def nasa_image():
    import requests
    nasa_api_key = DEMO_KEY  # Replace with your NASA API key
    nasa_url = "https://api.nasa.gov/planetary/apod"
    
    try:
        response = requests.get(f"{nasa_url}?api_key={nasa_api_key}")
        data = response.json()
        result = {
            'url': data['url'],
            'explanation': data['explanation'],
            'title': data['title'],
            'date': data['date']
        }
        return jsonify(result)
    except Exception as e:
        return jsonify({'message': f'Error fetching NASA picture: {str(e)}'})

@app.route('/api/button3', methods=['POST'])
def button3_action():
    # Add your button 3 logic here
    return jsonify({'message': 'Button 3 action completed'})

if __name__ == '__main__':
    app.run(debug=True)
