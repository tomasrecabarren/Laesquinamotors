from flask import Flask, request, render_template, redirect, url_for, session
import mysql.connector


app = Flask(__name__)

app.secret_key = 'supersecretkey'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="usuarios"
)

@app.route('/')
def index():
    if  'username' in session:
        return render_template('index.html', username=session['username'])
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre_usuario = request.form['nombre_usuario']
        contraseña = request.form['contraseña']
        cursor = db.cursor()
        cursor.execute("insert into usuarios (nombre_usuario, contraseña) values (%s, %s)", (nombre_usuario, contraseña))
        db.commit()
        cursor.close()
        session['username'] = nombre_usuario
        return redirect(url_for('index'))
    return render_template('registro.html')

@app.route('/login', methods=['GET','POST'])
def login(): 
    if request.method == 'POST':
        nombre_usuario = request.form.get['nombre_usuario']
        contraseña = request.form.get['contraseña']
        if nombre_usuario and contraseña:
            cursor = db.cursor()
        cursor.execute("select * from usuarios where nombre_usuario=%s and contraseña=%s", (nombre_usuario, contraseña))
        user = cursor.fetchone()
        cursor.close()
        if user:
            session['username'] = nombre_usuario
            return redirect(url_for('index'))
    else:
        return "Nombre de usuario o contraseña incorrectos"
    return render_template('login.html')

@app.route ('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

#////////////////////////////////////// Autos
@app.route('/mazda')
def mazda():
    return render_template('mazda.html') 

@app.route('/suzuki')
def suzuki():
    return render_template('suzuki.html') 

@app.route('/supra')
def supra():
    return render_template('supra.html')

@app.route('/Mirage')
def mirage():
    return render_template('mirage.html') 

#////////////////////////////////////////

if __name__ == '__main__':
    app.run(debug=True)
