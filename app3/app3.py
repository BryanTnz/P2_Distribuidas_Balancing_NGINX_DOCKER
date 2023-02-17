from flask import request, Flask
import json

app3 = Flask(__name__);

@app3.route('/')
def hello_world():
    return "Hola Bryan te saludo desde Flask en la APP 3"

if __name__ == '__main__':
    app3.run(debug=True, host = '0.0.0.0')

