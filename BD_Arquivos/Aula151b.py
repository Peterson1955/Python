from mysql.connector import connect

con = connect(
    host="localhost",
    port=3306,
    user="root",
    password="12345678"

)

print(type(con))




con.close()
