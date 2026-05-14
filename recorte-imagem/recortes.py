from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar ():
    nome = request.form.get("nome", "").strip()

    if not nome:
        return "Você não digitou nenhum nome."
    
    return f"Olá, {nome}. O backend recebeu seu formulário com sucesso"

@app.route("/upload", methods=["POST"])
def upload():
    if "imagem" not in request.files:
        return "Nenhuma imagem foi enviada."
    
    arquivo = request.files["imagem"]

    if arquivo.filename == "":
        return "Nenhum arquivo foi selecionado."
    

    
    nome_seguro = secure_filename(arquivo.filename)
    caminho_arquivo = os.path.join(UPLOAD_FOLDER, nome_seguro)
    arquivo.save(caminho_arquivo)

    return f"Upload dealizado com sucesso. Arquivo salvo em: {caminho_arquivo} "

if __name__ == "__main__":
    app.run(debug=True)

