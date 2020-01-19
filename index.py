from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #return "Hola mundo !"
    return render_template('inicio.html')

@app.route('/about')
def about():
    print ("ingreso en la ruta about")
    return "About"


if __name__ == '__main__':
    app.run(debug=True)