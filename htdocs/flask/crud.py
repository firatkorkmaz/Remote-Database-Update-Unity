from flask import Flask, request, render_template
import sqlite3  
  
app = Flask(__name__)  

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tables/records")
def records():
    con = sqlite3.connect("../register.db")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    
    cur.execute("SELECT CU_ID, NAME, AGE, GENDER, COUNTRY, JOB, EMAIL, PHONE FROM Customer INNER JOIN Info ON Customer.INFO_ID = Info.INFO_ID INNER JOIN Contact ON Info.CO_ID = Contact.CO_ID")
    rows = cur.fetchall()
    return render_template("tables/records.html", rows=rows)


##########################################

@app.route("/viewupdate", methods=['POST'])
def viewupdate():
    cu_id = request.form["cu_id"]
    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    country = request.form["country"]
    job = request.form["job"]
    email = request.form["email"]
    phone = request.form["phone"]

    con = sqlite3.connect("../register.db")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    
    if len(name) != 0:
        cur.execute("UPDATE Customer SET NAME = ? WHERE CU_ID = ?", [name, cu_id])
    if len(age) != 0:
        if age.isdigit():
            cur.execute("UPDATE Customer SET AGE = ? WHERE CU_ID = ?", [age, cu_id])
    if len(gender) != 0:
        cur.execute("UPDATE Customer SET GENDER = ? WHERE CU_ID = ?", [gender, cu_id])

    if len(country) != 0:
        cur.execute("UPDATE Info SET COUNTRY = ? WHERE INFO_ID = ?", [country, cu_id])
    if len(job) != 0:
        cur.execute("UPDATE Info SET JOB = ? WHERE INFO_ID = ?", [job, cu_id])

    if len(email) != 0:
        cur.execute("UPDATE Contact SET EMAIL = ? WHERE CO_ID = ?", [email, cu_id])
    if len(phone) != 0:
        cur.execute("UPDATE Contact SET PHONE = ? WHERE CO_ID = ?", [phone, cu_id])

    con.commit()
    cur.execute("SELECT CU_ID, NAME, AGE, GENDER, COUNTRY, JOB, EMAIL, PHONE FROM Customer INNER JOIN Info ON Customer.INFO_ID = Info.INFO_ID INNER JOIN Contact ON Info.CO_ID = Contact.CO_ID WHERE CU_ID = ?", [cu_id])
    rws = cur.fetchall()
    cur.execute("SELECT CU_ID, NAME, AGE, GENDER, COUNTRY, JOB, EMAIL, PHONE FROM Customer INNER JOIN Info ON Customer.INFO_ID = Info.INFO_ID INNER JOIN Contact ON Info.CO_ID = Contact.CO_ID")
    rows = cur.fetchall()
    return render_template("viewupdate.html", rows=rows, rws=rws)


@app.route("/delete", methods=['POST'])
def delete():
    cu_id = request.form["cu_id"]

    con = sqlite3.connect("../register.db")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    
    cur.execute("DELETE FROM Customer WHERE CU_ID = ?", [cu_id])
    cur.execute("DELETE FROM Info WHERE INFO_ID = ?", [cu_id])
    cur.execute("DELETE FROM Contact WHERE CO_ID = ?", [cu_id])
    cur.execute("UPDATE sqlite_sequence SET seq = (SELECT MAX(CU_ID) FROM Customer)");
    
    con.commit()
    cur.execute("SELECT CU_ID, NAME, AGE, GENDER, COUNTRY, JOB, EMAIL, PHONE FROM Customer INNER JOIN Info ON Customer.INFO_ID = Info.INFO_ID INNER JOIN Contact ON Info.CO_ID = Contact.CO_ID")
    rows = cur.fetchall()
    return render_template("tables/records.html", rows=rows)
    

@app.route("/insert", methods=['POST'])
def insert():
    cu_id = request.form["cu_id"]
    name = request.form["name"]
    age = request.form["age"]
    gender = request.form["gender"]
    country = request.form["country"]
    job = request.form["job"]
    email = request.form["email"]
    phone = request.form["phone"]

    con = sqlite3.connect("../register.db")
    con.text_factory = lambda b: b.decode(errors='ignore')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    
    cur.execute("INSERT INTO Contact (EMAIL, PHONE) VALUES (?, ?)", [email, phone])
    co_id=cur.lastrowid
    cur.execute("INSERT INTO Info (COUNTRY, JOB, CO_ID) VALUES (?, ?, ?)", [country, job, co_id])
    info_id=cur.lastrowid
    cur.execute("INSERT INTO Customer (NAME, AGE, GENDER, INFO_ID) VALUES (?, ?, ?, ?)", [name, age, gender, info_id])
    cur.execute("UPDATE sqlite_sequence SET seq = (SELECT MAX(CU_ID) FROM Customer)");
   
    con.commit()
    cur.execute("SELECT CU_ID, NAME, AGE, GENDER, COUNTRY, JOB, EMAIL, PHONE FROM Customer INNER JOIN Info ON Customer.INFO_ID = Info.INFO_ID INNER JOIN Contact ON Info.CO_ID = Contact.CO_ID")
    rows = cur.fetchall()
    return render_template("tables/records.html", rows=rows)



if __name__ == "__main__":
    app.run(debug = True)