from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
import math
import forms

app = Flask(__name__)
app.secret_key='Clave secreta'
csrf=CSRFProtect()

@app.route('/')
def home():
    titulo = "IDGS-802-Flask"
    lista = ['Raul', 'Pepe', 'Ana', 'Juan']
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route('/usuarios', methods=["GET", "POST"])
def usuarios():
    mat=0
    nom=''
    apa=''
    ama='' 
    email=''
    usuarios_class=forms.UserForms(request.form)
    if request.method=='POST' and usuarios_class.validate():
        mat=usuarios_class.matricula.data
        nom=usuarios_class.nombre.data
        apa=usuarios_class.apaterno.data
        ama=usuarios_class.amaterno.data
        email=usuarios_class.correo.data

        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)
        
    return render_template('usuarios.html', form=usuarios_class, mat=mat, nom=nom, apa=apa, ama=ama, email=email)

@app.route('/formularios')
def formularios():
    return render_template('formularios.html')

@app.route('/reportes')
def reportes():
    return render_template('reportes.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/hola')
def hola():
    return "Jola, Jola"

@app.route('/user/<string:user>')
def user(user):
    return "formulario"

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero: {}".format(n)

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "ID: {} nombre: {}".format(id, username)

@app.route('/suma/<float:n1>/<float:n2>')
def func(n1, n2):
    return "La suma es: {}".format(n1 + n2)

@app.route('/default/')
@app.route('/default/<string:param>')
def func2(param='Juan'):
    return f"<h1>Hola, {param}<h1>"

@app.route('/operas')
def operas():
    return '''
        <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="name">Apaterno:</label>
        <input type="text" id="name" name="name" required>
        </form>
    '''

@app.route("/operasBas", methods=["GET", "POST"])
def operas1():
    n1 = 0
    n2 = 0
    res = 0
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        res = float(n1) / float(n2)
    return render_template("operasBas.html", n1=n1, n2=n2, res=res)

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        operacion = request.form.get("op")
        try:
            num1 = float(n1)
            num2 = float(n2)
        except ValueError:
            return "Error"
        res = 0
        signo = ""
        if operacion == "suma":
            res = num1 + num2
            signo = "+"
        elif operacion == "resta":
            res = num1 - num2
            signo = "-"
        elif operacion == "multi":
            res = num1 * num2
            signo = "*"
        else:
            return "Error: No selecciono nada"
        return f"El resultado de: {num1} {signo} {num2} es {res}"
    return "No hay datos."

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    return render_template("alumnos.html")

@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    resultado = 0.0
    if request.method == "POST":
        x1 = float(request.form.get("X1"))
        y1 = float(request.form.get("Y1"))
        x2 = float(request.form.get("X2"))
        y2 = float(request.form.get("Y2"))
        resultado = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return render_template("distancia.html", dist=resultado)

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True, port=3000)

