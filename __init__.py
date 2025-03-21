from cryptography.fernet import Fernet
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <h1>Bienvenue sur l'API de chiffrement !</h1>
    <p>Utilisez les routes suivantes :</p>
    <ul>
        <li>/generate_key</li>
        <li>/encrypt/&lt;key&gt;/&lt;valeur&gt;</li>
        <li>/decrypt/&lt;key&gt;/&lt;token&gt;</li>
    </ul>
    """

# ✅ Génération de clé unique
@app.route('/generate_key')
def generate_key():
    key = Fernet.generate_key()
    return f"Voici votre clé personnelle : {key.decode()}"

# ✅ Route pour chiffrer avec une clé fournie
@app.route('/encrypt/<key>/<valeur>')
def encryptage(key, valeur):
    try:
        f = Fernet(key.encode())  # On utilise la clé fournie
        valeur_bytes = valeur.encode()
        token = f.encrypt(valeur_bytes)
        return f"Valeur encryptée : {token.decode()}"
    except Exception as e:
        return f"Erreur lors du chiffrement : {str(e)}"

# ✅ Route pour déchiffrer avec une clé fournie
@app.route('/decrypt/<key>/<token>')
def decryptage(key, token):
    try:
        f = Fernet(key.encode())  # On utilise la clé fournie
        token_bytes = token.encode()
        valeur_decryptee = f.decrypt(token_bytes)
        return f"Valeur décryptée : {valeur_decryptee.decode()}"
    except Exception as e:
        return f"Erreur lors du déchiffrement : {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
