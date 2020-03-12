import mysql.connector
from mysql.connector import Error
#connecto db    
def connect_sql():
    mydb = mysql.connector.connect(host="localhost",user="root", passwd="", database="test")
    return mydb

#execute query
def execute_sql(sql):
    try:
        mydb = connect_sql()
        mycursor = mydb.cursor()
        mycursor.execute(*sql)
        return mycursor, mydb
    except Error as error:
        print (error)
    
    
#close connection
def close_connect(mycursor, mydb):
    mycursor.close()
    mydb.close()

def select_data():
    sql = ("""select comm from blog""", ())
    
    mycursor, mydb = execute_sql(sql)

    record = mycursor.fetchall()

    close_connect(mycursor, mydb)
    return record


# insert data and return last insert id    
def insert_data(filename, id = None):
    if id is None:
        sql = ("""INSERT INTO testapi (name) VALUES (%s)""", (filename,))
    else:
        sql = ("""INSERT INTO testapi (name, id) VALUES (%s,%s)""", (filename,id,))
    
    try:
        mycursor, mydb = execute_sql(sql)
        mydb.commit()
        id = mycursor.lastrowid
        
    except Error as error:
        print (error)
    
    finally:
        close_connect(mycursor, mydb)
        return id


#update name in database 
def update_data(email, password):
    sql = ("""update csrf set pass = %s where email = %s """, (password, email,))
    mycursor, mydb = execute_sql(sql)
    mydb.commit()
    result = mycursor.rowcount
    close_connect(mycursor, mydb)
    return result

#delete data with id
def delete_data(id):
    sql = ("""delete from testapi where id = %s""", (id,))
    try:
        mycursor, mydb = execute_sql(sql)
        mydb.commit()
    except Error as error:
        print (error)
    finally:
        close_connect(mycursor, mydb)
        return True


def check_file_exits(id):
    sql = ("""select id from testapi where id = %s""", (id,))
    result = ()
    try:
        mycursor, mydb = execute_sql(sql)
        result = mycursor.fetchall()
        
    except Error as error: 
        print(error)
        
    finally:
        close_connect(mycursor, mydb)
        if result:
            return True
        else:
            return False