
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API V71 - Técnica Salomão está ativa e funcional!"

@app.route("/ping")
def ping():
    return jsonify({"status": "online", "message": "pong"})

@app.route("/status")
def status():
    return jsonify({
        "api": "loterias-api-v71",
        "versao": "1.0",
        "tecnica": "Salomão + V71",
        "status": "operacional"
    })

@app.route("/api/lotofacil/latest")
def lotofacil_latest():
    return jsonify({
        "modalidade": "Lotofacil",
        "concurso": 3450,
        "data": "2025-07-24",
        "dezenas": ["01", "03", "06", "08", "09", "10", "11", "13", "14", "17", "18", "19", "20", "23", "25"]
    })

@app.route("/api/mega-sena/latest")
def mega_sena_latest():
    return jsonify({
        "modalidade": "Mega-Sena",
        "concurso": 2892,
        "data": "2025-07-26",
        "dezenas": ["07", "12", "23", "35", "44", "58"]
    })

@app.route("/api/quina/latest")
def quina_latest():
    return jsonify({
        "modalidade": "Quina",
        "concurso": 6781,
        "data": "2025-07-26",
        "dezenas": ["03", "18", "25", "39", "71"]
    })

@app.route("/api/timemania/latest")
def timemania_latest():
    return jsonify({
        "modalidade": "Timemania",
        "concurso": 2272,
        "data": "2025-07-26",
        "dezenas": ["04", "12", "18", "24", "33", "40", "77"],
        "time_do_coracao": "Flamengo/RJ"
    })

@app.route("/api/dupla-sena/latest")
def dupla_sena_latest():
    return jsonify({
        "modalidade": "Dupla Sena",
        "concurso": 2621,
        "data": "2025-07-26",
        "sorteio_1": ["05", "12", "21", "33", "42", "48"],
        "sorteio_2": ["03", "14", "22", "35", "41", "45"]
    })

@app.route("/api/milionaria/latest")
def milionaria_latest():
    return jsonify({
        "modalidade": "+Milionária",
        "concurso": 158,
        "data": "2025-07-26",
        "dezenas": ["02", "10", "18", "28", "41", "47"],
        "trevos": ["1", "4"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
