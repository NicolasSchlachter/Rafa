from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/button_click', methods=['POST'])
def button_click():
    button_name = request.json.get('button_name')
    if button_name == 'Button 1':
        numbers = list(range(1, 100001))
        for number in numbers:
            print(number)
        return jsonify(result="Numbers printed up to 1000")
    else:
        return jsonify(result="Unknown button")

if __name__ == '__main__':
    app.run(debug=True)
