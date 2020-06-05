from flask import Flask
from flask import render_template
from conversation import *
from flask_socketio import SocketIO, send


app= Flask(__name__)
app.config["SECRET_KEY"]="secret"

conversation= Conversation()

socket= SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<user>")
def users(user):
    if not conversation.validate_member(user):
        conversation.members.append(user)
    
    return render_template("main.html", mess=conversation.to_string())

@socket.on("message")
def handle_message(info):
    print(info)
    send(info, broadcast=True)

if __name__=="__main__":
    #app.run( port=8000, debug=True )
    socket.run(app, port=8000, debug=True)
   
