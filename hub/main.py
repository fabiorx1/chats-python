from flask import Flask, jsonify, request

app = Flask(__name__)

enderecos = {}  # dict contendo os endereços IP registrados no HUB.

@app.route("/registro", methods=["POST"])
def registrar_host():
    host_address = request.remote_addr
    host_port = request.form["port"]

    # Adicionao IP do Host à lista do Hub
    enderecos[f"{host_address}:{host_port}"] = {"ip": host_address, "port": host_port}
    return jsonify({"mensagem": "Host registrado com sucesso!"})

@app.route("/hosts")
def ler_hosts():
    return jsonify(list(enderecos.keys()))

@app.route("/remover", methods=["DELETE"])
def remover_host():
    host_address = request.remote_addr
    host_port = request.form["port"]

    # Remove endereço do Host da lista do HUB
    del enderecos[f"{host_address}:{host_port}"]
    return jsonify({"mensagem": "O Host foi removido com sucesso!"})

if __name__ == "__main__":
    app.run()