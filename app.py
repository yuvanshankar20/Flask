from flask import Flask,redirect,url_for

app=Flask(__name__)

#https://www.techwithtim.net/tutorials/flask/a-basic-website

#Flask is a known as a micro web framework. 
# This means it provides some basic functionality to allow developers to build simple websites. 
# It does not come with all the bells and whistles like some other web frameworks like django have and therefore is typically not used for complex websites. 
# However, there is a benefit to flask's limited features.

@app.route("/")  # this sets the route to this page
def home():
	return "Hello! this the main page <h1>HELLO</h1>"

@app.route("/user/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="hello admin"))

if __name__ == "__main__":
	app.run()