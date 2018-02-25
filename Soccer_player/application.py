from flask import Flask, redirect, render_template, request, session, url_for
import sqlite3 as sql

# c.execute('''
# CREATE TABLE record(
# Name varchar(255) NOT NULL,
# Last varchar(255)
# );''')
app = Flask(__name__)
app.secret_key = "sjfgiefyhube"


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    connect = sql.connect('record.db')
    c = connect.cursor()

    if request.form["first"] == "" or request.form["last"] == "":
        return render_template("failure.html")

    # database
    c.execute("INSERT INTO record (Name, Last) VALUES(?,?)", (request.form["first"], request.form["last"]))
    connect.commit()
    e = c.execute("SELECT * FROM record WHERE Name= ?", (request.form.get("first"),)).fetchall()
    print(e[0][1])
    print(e)
    c.close()
    return render_template("success.html")


app.run("0.0.0.0", "8080")

# connect = sql.connect('record.db')
# c = connect.cursor()
# c.execute("SELECT * FROM record")
# print(c.fetchall())
