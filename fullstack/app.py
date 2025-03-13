from flask import Flask, render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    mobile = request.form['mobile']
    password = request.form['password']
    print(name,email,mobile,password)    
    # Here you can add code to save the data to a database    
    return redirect(url_for('signup'))

if (__name__ == '__main__'):
    app.run(debug=True)