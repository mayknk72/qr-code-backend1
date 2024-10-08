from flask import Flask, request, jsonify
import qrcode
import os
import json

app = Flask(__name__)

# Local para armazenar os dados de escaneamento
DATA_FILE = "data.json"

# Função para inicializar os dados
def initialize_data():
    if not os.path.exists(DATA_FILE):
        data = {
            "scans": 0,
            "max_scans": 10
        }
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f)

# Função para atualizar o número de escaneamentos
def update_scans():
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)

    if data["scans"] < data["max_scans"]:
        data["scans"] += 1
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f)
        return True
    return False

# Rota para gerar o QR Code
@app.route('/generate_qr', methods=['GET'])
def generate_qr():
    # Gerar um QR Code com uma URL específica
    url = "http://<YOUR_DOMAIN>/scan"
    qr = qrcode.make(url)
    qr_path = "qr_code.png"
    qr.save(qr_path)
    
    return jsonify({"message": "QR Code generated!", "qr_code_url": qr_path}), 200

# Rota para escanear o QR Code
@app.route('/scan', methods=['GET'])
def scan():
    initialize_data()
    if update_scans():
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return jsonify({"message": "Scan successful!", "remaining_scans": data["max_scans"] - data["scans"]}), 200
    else:
        return jsonify({"message": "Max scans reached!"}), 400

if __name__ == '__main__':
    app.run(debug=True)
