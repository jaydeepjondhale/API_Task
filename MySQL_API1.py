import mysql.connector as conn

from flask import Flask, request, jsonify


# connecting to mysql and creating database, table
mydb = conn.connect(host="localhost",user='root',passwd='Jroot')
cursor = mydb.cursor() # cursor for database
cursor.execute('CREATE DATABASE IF NOT EXISTS users')
cursor.execute('CREATE TABLE IF NOT EXISTS users.user_pass(username varchar(20), password varchar(20))')


app = Flask(__name__)

# Insert function
""" 
for insertion request format is :
    { "username" : "Jaydeep",
       "password" : "jaydeep@api" 
    }
    
    -> use this above format while sending requst to insert data from postman...

"""
@app.route('/user/insert',methods=['GET','POST'])
def insert():
    if(request.method=='POST'):
        try:
            name = request.json['username']
            passwd = request.json['password']
            q1 = 'INSERT INTO users.user_pass(username,password) values(%s,%s)'
            val1 = (name, passwd)
            cursor.execute(q1, val1)
            mydb.commit()
            return jsonify((str(cursor.rowcount) + " row(s) Inserted Successfully"))
        except Exception as e:
            return jsonify((str(e)))



# update
""" 
for insertion request format is :
    { "username" : "Jaydeep",
       "new_password" : "api@1234" 
    }

    -> use this above format while sending requst to update data from postman...

"""
@app.route('/user/update', methods=['GET', 'POST'])
def update():
    if (request.method == 'POST'):
        try :
            name = request.json['username']
            passwd = request.json['new_password']
            q1 = 'UPDATE users.user_pass SET password= %s where username= %s'
            val1 = (passwd, name)
            cursor.execute(q1, val1)
            mydb.commit()
            return jsonify((str(cursor.rowcount) + " row(s) Updated Successfully"))
        except Exception as e:
            return jsonify((str(e)))


# Delete
""" 
for insertion request format is :
    { 
       "username" : "Jaydeep" 
    }

    -> use this above format while sending requst to delete data from postman ...

"""

@app.route('/user/delete', methods=['GET', 'POST'])
def delete():
    if (request.method == 'POST'):
        try :
            name = request.json['username']
            q1 = "DELETE FROM users.user_pass WHERE username = %s"
            val1 = (name,)
            cursor.execute(q1, val1)
            mydb.commit()
            return jsonify((str(cursor.rowcount) + " row(s) Deleted Successfully"))
        except Exception as e:
            return jsonify((str(e)))


# fetch data
""" 
for insertion request format is :
    { 
      "request" : "fetch" 
    }

    -> use this above format while sending requst to fetch data from postman...

"""
@app.route('/user/fetch', methods=['GET', 'POST'])
def fetch():
    if (request.method == 'POST'):
        try :
            name = request.json['request']
            if name == 'fetch':
                q1 = "SELECT * FROM users.user_pass"
                cursor.execute(q1)
                d1={}
                for i,j in cursor.fetchall():
                    d1[i] = j;
                return jsonify(d1)
        except Exception as e:
            return jsonify((str(e)))





if __name__ == '__main__' :
    app.run()








