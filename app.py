from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify(message="Hello, World!")

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()

    if 'num1' not in data or 'num2' not in data:
        return jsonify(error="Missing 'num1' or 'num2' in request data"), 400

    num1 = data['num1']
    num2 = data['num2']

    try:
        result = num1 + num2
        return jsonify(result=result)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
