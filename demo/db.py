# connecct to pythonanywhere mysql database
import json
import pymysql
import pymysql.cursors
domain = 'Scrapy97.mysql.pythonanywhere-services.com'
user = 'Scrapy97'
password = 'Qwerty@98'
db = 'Scrapy97$booking'
connection = pymysql.connect(host=domain,
                             user=user,
                             password=password,
                             db=db,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
# Create a new record
# with connection.cursor() as cursor:
#     # create test table
#     sql = "CREATE TABLE IF NOT EXISTS `test` (`id` int(11) NOT NULL AUTO_INCREMENT,`name` varchar(100) NOT NULL,`age` int(11) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
#     cursor.execute(sql)
#     # insert data
#     sql = "INSERT INTO `test` (`name`, `age`) VALUES (%s, %s)"
#     cursor.execute(sql, ('Bob', 21))
#     # read data
#     sql = "SELECT `id`, `name`, `age` FROM `test` WHERE `name`=%s"
#     cursor.execute(sql, ('Bob',))
#     result = cursor.fetchall()
#     print(result)
# # connection is not autocommit by default. So you must commit to save
# # your changes.
# connection.commit()
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        with connection.cursor() as cursor:
            sql = "INSERT INTO `test` (`name`, `age`) VALUES (%s, %s)"
            cursor.execute(sql, (name, age))
        connection.commit()
    
        return 'Data inserted successfully'

@app.route('/read', methods=['GET'])
def read():
    if request.method == 'GET':
        with connection.cursor() as cursor:
            sql = "SELECT `id`, `name`, `age` FROM `test`"
            cursor.execute(sql)
            result = cursor.fetchall()
        return json.dumps(result)

@app.route('/', methods=['GET'])
def index():
    return 'Hello Booking.com'