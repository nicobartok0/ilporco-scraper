from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/post_datos/<datos>')
def post_datos(datos):
    return datos

@app.route('/get_datos')
def get_datos():
    return 'Hola mundo'