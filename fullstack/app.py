from flask import Flask, render_template,request,redirect,url_for,flash
import pymysql
app = Flask(__name__)
app.secret_key = 'test'
# Database connection
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='kaushalya@2017',
        db='demodb',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


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
    # 
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO user (name, email, mobile, password) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (name, email, mobile, password))
        connection.commit()
        flash('Registration successful!', 'success')

    finally:
        connection.close()
      
    return redirect(url_for('signup'))

if (__name__ == '__main__'):
    app.run(debug=True)