import os
import sqlite3

if(os.path.exists("./register.db")):
    print("Database: \"register.db\" already exists!")

else:
    con = sqlite3.connect("register.db")  
    print("Database: \"register.db\" is created successfully.")  

    con.execute("CREATE TABLE Contact (CO_ID INTEGER PRIMARY KEY AUTOINCREMENT, EMAIL varchar(50) UNIQUE, PHONE varchar(50) UNIQUE)")
    con.execute("CREATE TABLE Customer (CU_ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME varchar(50), AGE INTEGER, GENDER varchar(50), INFO_ID INTEGER REFERENCES Info (INFO_ID))")
    con.execute("CREATE TABLE Info (INFO_ID INTEGER PRIMARY KEY AUTOINCREMENT, COUNTRY varchar(50), JOB varchar(50), CO_ID INTEGER REFERENCES Contact (CO_ID))")
    
    con.close()
    print("Tables: \"Contact\", \"Customer\", \"Info\" are created successfully.")  

    