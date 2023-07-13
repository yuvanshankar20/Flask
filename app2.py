from flask import Flask,render_template,url_for,redirect
app=Flask(__name__)

#Creating a Base Template
#So you may have realized that creating new web pages for every single page on our website is extremely inefficient. 
# Especially when our website follows a theme and has similar elements (like a sidebar) on every page. 
# This is where template inheritance comes in. 
# We will talk about how to inherit HTML code later but we are going to start by creating a new HTML document called "base.html". 
# This will hold all of the HTML code that will persist throughout our website.

@app.route("/")
@app.route("/home")
def home():
    return render_template("index2.html")

@app.route("/ind")
def ind():
    return render_template("index2.1.html")

if __name__ == "__main__":
    app.run(debug=True)