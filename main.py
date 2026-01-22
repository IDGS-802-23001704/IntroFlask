from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def home():
    titulo="IDGS-802-Flask"
    lista= ['Raul','Pepe','Ana', 'Juan']
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route('/formularios')
def formularios():
    return render_template('formularios.html')

@app.route('/reportes')
def reportes():
    return render_template('reportes.html')

@app.route('/index')
def index():
    return render_template(index.html)

@app.route('/hola')
def hola():
    return "Jola, Jola"

@app.route('/user/<string:user>')
def user(user):
    return ("formulario")

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero: {}" .format(n)

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "ID: {} nombre: {}" .format(id, username)

@app.route('/suma/<float:n1>/<float:n2>')
def func(n1, n2):
    return "La suma es: {}" .format(n1+n2)

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

@app.route("/operasBas")
def operas1():
    return render_template("operasBas.html")

@app.route("/resultado", methods={"GET","POST"})
def resultado():
    n1=request.form.get("n1")
    n2=request.form.get("n2")
    return f"La suma es: {float(n1)+float(n2)}"



if __name__=='__main__':
    app.run(debug=True)

