from flask import request, Flask
import json

app4 = Flask(__name__);

@app4.route('/')
def hello_world():
    return "Hola Bryan te saludo desde Flask en la APP 4"

if __name__ == '__main__':
    app4.run(debug=True, host = '0.0.0.0')

