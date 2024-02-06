from flask_cors import CORS
from flask import Flask, jsonify
import math as mt

app = Flask(__name__)
CORS(app)

# index principal 
@app.route('/')
def principal():
    return 'En la URL define /(Operacion)/(numero1)/(numero2)'

# suma 
@app.route('/suma/<float:numero1>/<float:numero2>')
@app.route('/suma/<int:numero1>/<int:numero2>')
@app.route('/suma/<int:numero1>/<float:numero2>')
@app.route('/suma/<float:numero1>/<int:numero2>')
def suma(numero1, numero2):
    resultado = numero1 + numero2
    data = {
        'resultado': resultado,
        'operacion': 'Suma'
    }
    return jsonify(data)

# resta 
@app.route('/resta/<float:numero1>/<float:numero2>')
@app.route('/resta/<int:numero1>/<int:numero2>')
@app.route('/resta/<int:numero1>/<float:numero2>')
@app.route('/resta/<float:numero1>/<int:numero2>')
def resta(numero1, numero2):
    resultado = numero1 - numero2
    data = {
        'resultado': resultado,
        'operacion': 'Resta'
    }
    return jsonify(data)

# multiplicacion 
@app.route('/multiplicacion/<float:numero1>/<float:numero2>')
@app.route('/multiplicacion/<int:numero1>/<int:numero2>')
@app.route('/multiplicacion/<int:numero1>/<float:numero2>')
@app.route('/multiplicacion/<float:numero1>/<int:numero2>')
def multiplicacion(numero1, numero2):
    resultado = numero1 * numero2
    data = {
        'resultado': resultado,
        'operacion': 'Multiplicacion'
    }
    return jsonify(data)

# division 
@app.route('/division/<float:numero1>/<float:numero2>')
@app.route('/division/<int:numero1>/<int:numero2>')
@app.route('/division/<int:numero1>/<float:numero2>')
@app.route('/division/<float:numero1>/<int:numero2>')
def division(numero1, numero2):
    resultado = numero1 / numero2
    data = {
        'resultado': resultado,
        'operacion': 'Division'
    }
    return jsonify(data)

# potenciacion 
@app.route('/potenciacion/<float:numero1>/<float:numero2>')
@app.route('/potenciacion/<int:numero1>/<int:numero2>')
@app.route('/potenciacion/<int:numero1>/<float:numero2>')
@app.route('/potenciacion/<float:numero1>/<int:numero2>')
def potenciacion(numero1, numero2):
    resultado = numero1 ** numero2
    data = {
        'resultado': resultado,
        'operacion': 'Potenciacion'
    }
    return jsonify(data)

# seno 
@app.route('/seno/<float:numero1>')
@app.route('/seno/<int:numero1>')
def seno(numero1):
    resultado = mt.sin(numero1)
    data = {
        'resultado': resultado,
        'operacion': 'Seno'
    }
    return jsonify(data)

# coseno 
@app.route('/coseno/<float:numero1>')
@app.route('/coseno/<int:numero1>')
def coseno(numero1):
    resultado = mt.cos(numero1)
    data = {
        'resultado': resultado,
        'operacion': 'Coseno'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
