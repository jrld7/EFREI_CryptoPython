from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html')

key = b'l--pTYAHzSJr35e4tlTA_5iACnolLqBt8cQA0ArM9D8='
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str t

@app.route('/decrypt/<string:token>')
def decryptage(token):
    try:
        token_bytes = token.encode()  # Conversion str -> bytes
        valeur_decryptee = f.decrypt(token_bytes)  # Déchiffre la valeur
        return f"Valeur décryptée : {valeur_decryptee.decode()}"  # Retourne en str
    except Exception as e:
        return f"Erreur lors du déchiffrement : {str(e)}"
                                                                                                                                                     
if __name__ == "__main__":
  app.run(debug=True)
