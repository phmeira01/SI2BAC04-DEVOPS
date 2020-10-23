import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(_name_)

@app.route('/')
def fibonacci()
proximo = 1
anterior = 0
limite = 50
f = 0
resposta = "0,"
while (f < limite):
    tmp = proximo
    proximo = proximo + anterior
    anterior = tmp
    f = f + 1
    resposta+= str(proximo)+ ","

return(resposta)

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
