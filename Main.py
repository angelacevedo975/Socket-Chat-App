from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, send


app= Flask(__name__)
app.config["SECRET_KEY"]="secret"

socket= SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<user>")
def users(user):
    return render_template("main.html", user=user )

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@socket.on("message")
def handle_message(info):
    send(info, broadcast=True)

if __name__=="__main__":
    #app.run( port=8000, debug=True )
    socket.run(app, port=8000, debug=True)
   
