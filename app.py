import glob
import io
import os
import uuid
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

#Clave secreta de la aplicacion
app.secret_key = '123456789'
app.debug = False
app._static_folder = os.path.abspath("/templates")

@app.route('/')
def index():
    return render_template('login.html')
    
@app.route('/incio')
def juego():
    return render_template('index.html')

@app.route('/start')
def inicio():
    return render_template('fase2.html')

#Metodo para correr la aplicacion
if __name__ == '__main__':
    app.run(debug=True)