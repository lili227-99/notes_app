from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
import mysql.connector

app = Flask(__name__)

Connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='liliana',
    database='taller'
)
print("Conexión exitosa a la base de datos")



@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route( '/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process login logic here
        pass
    return render_template('login.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')


@app.route('/servicios')
def servicios():
    return render_template('servicios.html')


@app.route('/motos')
def motos():
    return render_template('motos.html')


@app.route('/historial')
def historial():
    return render_template('historial.html')

if __name__ == '__main__':
    app.run(debug=True)