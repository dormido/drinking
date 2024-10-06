from flask import Flask, render_template, request
from functions import get_translations, data, calc

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        language = request.form["language"]
        gender = int(request.form["gender"])
        weight = float(request.form["weight"])
        tam = int(request.form["tam"])
        drink = int(request.form["drink"])

        k, tma, wh, grad = data(gender, weight, tam, drink)
        hundred = 100
        density = 0.8
        cai = calc(tma, k, wh, hundred, density, grad)

        return render_template("index.html", result=cai)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
