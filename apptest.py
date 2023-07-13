from flask import Flask,redirect,url_for,request,render_template

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("login.html")

#URL binding for Flask app and  Flask admin routes  

@app.route("/admin")
def admin():
    return "Hello admin"

@app.route("/guest")
def guest():
    name=request.args.get("name")
    return f"Hello {name}"

@app.route("/user/<name>")
def user(name):
    if name =="admin":
        return redirect(url_for("admin"))
    else:
        return redirect(url_for("guest",name=name))

#variable in flask contains int and float

@app.route("/blog/<int:id>")
def blog(id):
    return f"Hello, {str(id)}"

@app.route("/log/<float:num>")
def blog_float(num):
    return f"Hello,{str(num)}"

#HTTP request
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        return render_template('login.html')
    
#Flask template
@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

# @app.route("/result/<name>")
# def name(name):
#     return render_template('result.html', names = name)
    

@app.route('/success/<name>', methods=['POST', 'GET'])
def success(name):
    return f'welcome <h1>{name}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
