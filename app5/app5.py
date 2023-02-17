from flask import request, Flask
import json

app5 = Flask(__name__);

@app5.route('/')
def hello_world():
    return "Hola Bryan te saludo desde Flask en la APP 5"

if __name__ == '__main__':
    app5.run(debug=True, host = '0.0.0.0')

