from logging import disable
from flask import Flask,render_template
from flask.globals import request
import pymysql

app = Flask(__name__)

# 資料庫設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "0000",
    "db": "text",
    "charset": "utf8"
}

#data base


@app.route("/")
def home():
    
    return render_template("mainpage.html")



@app.route("/get",methods=["POST"])
def test1():

    conn = pymysql.connect(**db_settings)
    message= request.form.get('text')

    list=[]
    #put something in mysql
    try:
    # 建立Connection物件
    # 建立Cursor物件
        with conn.cursor() as cursor:
            command = "INSERT INTO string VALUES(%s)"
            cursor.execute(
            command,(message)
            )
            cursor.execute("SELECT * FROM string")
            displaytext = cursor.fetchall()
            for text in displaytext:
                list.append(text[0])

            conn.commit()
            return render_template("mainpage.html",messages=list,)      
        
    except Exception as ex:
        print(ex)
    
    

app.run(port=3333)
