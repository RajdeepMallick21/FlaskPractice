from http.cookiejar import uppercase_escaped_char

from flask import Flask, render_template

# Create a flask instance
app = Flask(__name__)

#Create a route decorator
@app.route('/')

# FILTERS
#safe
#capitalize
#lower
#upper
#title
#trim
#striptags


def index():
    #return "<h1>Hello World</h1>"
    first_name="John"
    stuff="This is <strong>bold text</strong>"
    favorite_pizza=["Pepperoni","Cheese","Mushroom", 41]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)

#localhost:5000/user/John
@app.route('/user/<name>')

def user(name):
    #return "<h1>Hello {}!!!</h1>".format(name)
    return render_template("user.html", user_name=name)

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
