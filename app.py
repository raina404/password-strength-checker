from flask import Flask, request, render_template
from password_checker import check_strength

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    password = request.form.get("password", "")
    result = check_strength(password)
    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
