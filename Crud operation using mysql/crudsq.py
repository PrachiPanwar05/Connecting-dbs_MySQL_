# ..........................CRUD operation of mysql into pycharm.....................................
#.........................................create database
# pip install mysql
# pip install mysql.connector
# pip install mysql-python-connector
# import mysql.connector
# mysqldb=mysql.connector.connect(host="localhost",user="root",password="0522",auth_plugin="mysql_native_password")
# mycursor=mysqldb.cursor()
# mycursor.execute("create database unique2")
# print("data base are created")
# mysqldb.close()


#create table.....................
# import mysql.connector
# mysqldb=mysql.connector.connect(host="localhost",user="root",password="0522",database="unique2",auth_plugin="mysql_native_password")
# mycursor=mysqldb.cursor()
# mycursor.execute("create table student01(roll int,name varchar(10), marks int)")
# mysqldb.close()

#insert value in student table
# import mysql.connector
# mysqldb=mysql.connector.connect(host="localhost",user="root",password="0522",database="unique2")
# mycursor=mysqldb.cursor()
# try:

#    mycursor.execute("insert into student01 values(1,'Mohit',80),(2,'Kunal',89),(3,'Harry',90)")
#    mysqldb.commit()
#    print('Record inserted successfully...')
# except:

#    print("error")
# mysqldb.close()


# display all data into console
# import mysql.connector
# mysqldb=mysql.connector.connect(host="localhost",user="root",password="0522",database="unique2")
# mycursor=mysqldb.cursor()
# try:
#    mycursor.execute("select * from student01")
#    result=mycursor.fetchall()
#    for i in result:
#       roll=i[0]
#       name=i[1]
#       marks=i[2]
#       print(roll,name,marks)
# except:
#    print('Error:Unable to fetch data.')
# mysqldb.close()
# #
# update data into table
# import mysql.connector
# mysqldb=mysql.connector.connect(host="localhost",user="root",password="0522",database="unique2")#established connection between your database
# mycursor=mysqldb.cursor()#cursor() method create a cursor object
# try:
#    mycursor.execute("UPDATE student01 SET roll='5', marks=100 WHERE roll=1")#Execute SQL Query to update record
#    mysqldb.commit() # Commit is used for your changes in the datsabase
#    print('Record updated successfully...')
# except Exception as e:
#    # rollback used for if any error
#    mysqldb.rollback()
#    print(e)
# mysqldb.close()#Connection Close
# #

#delete command of rollno 3
import mysql.connector
mysqldb=mysql.connector.connect(host="localhost",user="root",password="0522",database="unique2")#established connection between your database
mycursor=mysqldb.cursor()#cursor() method create a cursor object
try:
   mycursor.execute("DELETE FROM student01 WHERE name='Mohit'")#Execute SQL Query to detete a record
   mysqldb.commit() # Commit is used for your changes in the database
   print('Record deteted successfully...')
except:
   # rollback used for if any error
   mysqldb.rollback()
mysqldb.close()#Connection Close