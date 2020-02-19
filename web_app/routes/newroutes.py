
from flask import Blueprint, request, render_template

newroutes = Blueprint("newroutes", __name__)

@newroutes.route("/books_home")
def newindex():
    print("VISITING THE NEW INDEX PAGE")
    return render_template("newhomepage.html")
