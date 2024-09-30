from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro')
def registro():
    return render_template('registro.html') 

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
