from flask import Flask, jsonify, request

app = Flask(__name__)

def calculate_results(marks_list):
    if not marks_list:
        return {"total": 0, "average": 0.0}
    total = sum(marks_list)
    average = total / len(marks_list)
    return {"total": total, "average": round(average, 2)}

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json() or {}
    marks = data.get("marks", [])
    results = calculate_results(marks)
    return jsonify(results), 200

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)