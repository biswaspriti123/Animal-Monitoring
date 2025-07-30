from flask import Flask, request, jsonify

app = Flask(__name__)
animals = {}

@app.route('/')
def home():
    return "Animal Monitoring API Running!"

@app.route('/update', methods=['POST'])
def update():
    data = request.json
    tag = data['tag']
    animals[tag] = data
    return jsonify({"status": "ok"})

@app.route('/animals', methods=['GET'])
def get_animals():
    return jsonify(animals)

if __name__ == '__main__':
    app.run(debug=True)
