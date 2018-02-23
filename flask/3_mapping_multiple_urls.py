# Exercise on mapping multiple URLs
# Ex: Show a different home page depending on whether a user is logged in or not

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<user>")
def index(user=None):
    return render_template("user.html",user=user)


if __name__ == "__main__":
    app.run()
