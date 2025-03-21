from cryptography.fernet import Fernet
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Bienvenue sur l'API de chiffrement !"

# ✅ Route POST /encrypt avec clé personnelle
@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    valeur = data.get('valeur')
    key = data.get('key')

    if not valeur or not key:
        return jsonify({'error': 'valeur et key sont requis'}), 400

    try:
        f = Fernet(key.encode())
        token = f.encrypt(valeur.encode())
        return jsonify({'token': token.decode()})
    except Exception as e:
        return jsonify({'error': f"Erreur de chiffrement : {str(e)}"}), 400

# ✅ Route POST /decrypt avec clé personnelle
@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    token = data.get('token')
    key = data.get('key')

    if not token or not key:
        return jsonify({'error': 'token et key sont requis'}), 400

    try:
        f = Fernet(key.encode())
        valeur = f.decrypt(token.encode())
        return jsonify({'valeur': valeur.decode()})
    except Exception as e:
        return jsonify({'error': f"Erreur de déchiffrement : {str(e)}"}), 400

# ✅ Route optionnelle pour générer une clé Fernet
@app.route('/generate_key', methods=['GET'])
def generate_key():
    key = Fernet.generate_key()
    return jsonify({'key': key.decode()})

if __name__ == "__main__":
    app.run(debug=True)
