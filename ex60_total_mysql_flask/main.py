# pip install flask flask-mysqldb werkzeug python-dotenv

# create table book{
#     bookid int primary key auto_increment,
#     bookname varchar(40) not null,
#     publisher varcher(40),
#     price int
# );

# create table customer{
#     custid int primary key auto_increment,
#     name varchar(40) not null,
#     address varchar(40),
#     phone varchar(40),
#     password varchar(255) not null
# );

# create table orders(
#     orderid int primary key auto_increment,
#     custid int, bookid int,
#     saleprice int, orderdate date,
#     foreign key(custid) references customer (custid) on delete cascade,
#     foreign key(bookid) references book (bookid) on delete cascade
# );

# on delete cascade : 책/고객이 삭제되면 연결된 데이터 삭제

# CRUD    SQL     WEB(restful api)
# --------------------------------------------------------
# CREATE  INSERT  POST
# READ    SELECT  GET
# UPDATE  UPDATE  PUT(한줄 전체 교체) or fetch(특정 값만 바꿈)
# DELETE  DELETE  DELETE

from flask import Flask, render_template, request, jsonify, session, url_for, redirect
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from dotenv import load_dotenv
import os

#env file 을 관리하는 이유: 깃허브 올릴때 깃이그노어 파일에 env를 등록

load_dotenv()

app = Flask(__name__)
app.secret_key=os.getenv('FLASK_SECRET_KEY')
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

def is_logged_in():
    return 'logged_in' in session

@app.route('/')
def index():
    if is_logged_in(): 
        return render_template('login.html') #redirect(url_for('/books_page'))
    return render_template('login.html')

@app.route('/register_page')
def register_page():
    return render_template('register.html')


#수신하고 DB에 insert. (비밀번호는 암호화)
@app.route('/api/register', methods=['POST'])
def api_register(): 
    data = request.get_json()
    hashed_pw = generate_password_hash(data['password'])
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO customer(name, address, phone, password) VALUES(%s, %s, %s, %s)", (data['name'], data['address'], data['phone'], hashed_pw))
    mysql.connection.commit()
    cur.close()
    return jsonify({"success":True, "message": "회원 가입 잘 되었읍니다"})
    
@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customer WHERE name=%s", (data['name'],))
    user = cur.fetchone()
    cur.close()
    if user and check_password_hash(user['password'], data['password']):
        session.update({'logged_in' : True, 'custid':user['custid'], 'name':user['name']})
        return jsonify({"success":True})
    return jsonify({"success":False, "message" : "ID, or PW 통과 못함"}), 401  #체크하지 않으면 이 라인으로 넘어오고 401메세지를 날린다.

if __name__ == "__main__" :
    app.run(debug=True, port=5000, host='127.0.0.1')