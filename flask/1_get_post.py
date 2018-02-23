# Flask exercises for interpreting GET and POST requests

from flask import Flask, request

app = Flask(__name__)


# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route("/")
def index():
    return "Method used: %s" % request.method

# GET the /tuna path
@app.route("/tuna")
def tuna():
    return '<h2>Tuna is good</h2>'

# GET with a username variable
@app.route("/profile/<username>")
def profile(username):
    return "Hey there %s" % username

# GET with an integer variable
@app.route("/post/<int:post_id>")
def show_post(post_id):
    return "<h2>Post ID is %s</h2>" % post_id

# POST method, add as a parameter to the route
@app.route("/bacon", methods=['GET', 'POST'])
def bacon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are probably using GET"


if __name__ == "__main__":
    app.run(debug=True)
