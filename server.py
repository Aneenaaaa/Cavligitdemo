from flask import Flask, request, jsonify

app = Flask(__name__)

stored_data = {}
@app.route('/greet', methods=['GET'])
def greet():
    if stored_data:
        name = stored_data.get('name', 'stranger')
    else:
        name = 'stranger'
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/clear', methods=['DELETE'])
def clear():
    global stored_data
    stored_data = {}  # Clear the stored data
    return jsonify({"message": "Stored data deleted."})


@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({"you_sent": data})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
