from flask import Flask,redirect,render_template,url_for,request
app = Flask(__name__)

#Information is exchanged between the client and the server using an HTTP protocol that has a few different methods. 
# We will be discussing the post commonly used ones called POST & GET.

#GET
#GET is the most commonly used HTTP method and it is typically used to retrieve information from a web server.

#POST
#POST is commonly used to send information to web server. 
# It is more often used when uploading a file, getting form data and sending sensitive data. 
# POST is a secure way to send data to a web server.

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        users=request.form["nm"]
        return redirect(url_for("user",usr=users))
    else:
        return render_template("index3.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)