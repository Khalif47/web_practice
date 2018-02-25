from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "sjfgiefyhube"


@app.route("/", methods=["POST", "GET"])
def board():
    if request.method == "POST":
        for item in ["aguero", "suarez"]:
            if item not in session:
                session[item] = int(request.form[item])
            else:
                session[item] += int(request.form[item])
        return redirect(url_for("goals"))
    return render_template("board.html")


@app.route("/goals")
def goals():
    goals = []
    for item in ["aguero", "suarez"]:
        goals.append({"name": item.capitalize(), "goal": session[item]})
    return render_template("goals.html", goals=goals)


@app.route("/highest")
def highest():
    result = []
    if session["aguero"] > session["suarez"]:
        n = "aguero"
        result.append({"name": n, "max": session["aguero"]})
    else:
        n = "suarez"
        result.append({"name": n, "max": session["suarez"]})
    return render_template("maximum.html", result=result)


app.run("0.0.0.0", "8080")
