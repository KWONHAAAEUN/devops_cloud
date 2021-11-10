from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    like_foods = ["떡볶이", "궁중떡볶이", "치즈떡볶이", "라볶이"]
    return render_template("profile.html", like_foods=like_foods)


@app.route("/posts")
def post_list():
    return render_template("post_list.html")
