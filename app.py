# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Hojare" # write your name
    age = "10" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/dad")
def home():

    name = "Keisuke" # write your name
    age = "54 or smthn idk" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage
@app.route("/mom")
def home():

    name = "Nao" # write your name
    age = "45" # write your age

    return render_template('index.html' , name = name , age = age)

@app.route("/friends")
def home():

    name = "Tony" # write your name
    age = "11" # write your age

    return render_template('index.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
