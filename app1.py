from flask import Flask,redirect,url_for,render_template
app=Flask(__name__)

#Flask uses a templating engine called jinja. 
# This allows you to write python code inside your html files. 
# It also allows you to pass information from your back-end (the python script) to your HTML files.
#In your HTML file you can use the following syntax to evaluate python statements. 
# {{Variable/Statement}} Placing a variable or statement inside of {{}} will tell flask to evaluate 
# the statement inside the brackets and render the text equivalent to it.
#You can place python expressions inside {% %}.
@app.route("/")
def home():
    return render_template("index.html",content="true")
    
if __name__ == "__main__":
    app.run()