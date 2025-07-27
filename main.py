from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API V71 funcionando corretamente!"

@app.route("/api/lotofacil/latest")
def lotofacil_latest():
    return jsonify({"concurso": 3450, "dezenas": ["01", "03", "06", "08", "09", "10", "11", "13", "14", "17", "18", "19", "20", "23", "25"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
