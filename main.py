from requests import Response
from flask import Flask, render_template, jsonify
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

if __name__ == '__main__':
    app.run(debug=True)
