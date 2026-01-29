from flask import Flask

app = Flask(__name__)

@app.route("/") #@ es un decorador: una sintaxis especial para modificar el comportamiento de funciones o clases de manera elegante
def hello_world():
    return "<p>Hello, World! hola hola hola</p>"