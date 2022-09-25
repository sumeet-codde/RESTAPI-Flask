from unittest import result
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/even/<int:a>')
def even(a):
    if (a%2==0):
        result={
            "number":a,
            "Even":True,
            "server ip":'122.122.12.1'
        }
    else:
        result={
            "number":a,
            "Even":False,
            "server ip":'122.122.12.1'
        }
    return jsonify(result)
    

if __name__ == '__main__':
    app.run(debug=True)