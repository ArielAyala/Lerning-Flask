from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola mundo !"

@app.route('/about')
def about():
    print ("ingreso en la ruta about")
    return "About"


if __name__ == '__main__':
    app.run()