# Exercise on passing objects (like a Python list) into templates
# Ex: Passing through a shopping list

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/shopping")
def shopping():
    food = ["Cheese", "Tuna", "Beef", "Toothpaste"]
    return render_template("shopping.html", food=food)


if __name__ == "__main__":
    app.run()
