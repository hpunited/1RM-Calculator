from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/1rm', methods=['POST'])
def calculate_one_rm():
    data = request.get_json()
    if not data or 'weight' not in data or 'reps' not in data:
        return jsonify(error="Verstrek zowel 'weight' als 'reps' in de JSON-body"), 400
    weight = float(data['weight'])
    reps = int(data['reps'])
    if reps <= 0 or weight <= 0:
        return jsonify(error="Gewicht en herhalingen moeten positief zijn"), 400
    one_rm = round(weight * (1 + reps / 30), 2)
    return jsonify(weight=weight, reps=reps, one_rm=one_rm)

if __name__ == '__main__':
    app.run(debug=True)
