from flask import Flask, jsonify

app = Flask(__name__)

# Dicionário para armazenar o número de escaneamentos por QR Code
qr_code_scans = {
    "qr_code_id": 10  # QR Code começa com 10 pontos
}

@app.route('/scanner/<qr_code_id>', methods=['GET'])
def scan_qr_code(qr_code_id):
    # Verifica se o QR Code existe
    if qr_code_id not in qr_code_scans:
        return jsonify({"message": "QR Code inválido!"}), 404
    
    # Verifica se o QR Code já foi escaneado 10 vezes
    if qr_code_scans[qr_code_id] <= 0:
        return jsonify({"message": "Limite de escaneamentos atingido!"}), 403
    
    # Reduz 1 ponto
    qr_code_scans[qr_code_id] -= 1
    return jsonify({"message": "QR Code escaneado com sucesso!", "pontos_restantes": qr_code_scans[qr_code_id]}), 200

if __name__ == '__main__':
    app.run(debug=True)

print ("menos 1 gole")