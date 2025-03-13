from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/welcome')
def welcome():
    return 'welcome to flask course'

@app.route('/add', methods=['GET'])
def add():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return str(a + b)
#for testing http://127.0.0.1/add?a=10&b=20

@app.route('/subtract', methods=['GET'])
def subtract():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return str(a - b)
if __name__ == '__main__':
    app.run()