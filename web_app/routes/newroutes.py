
from flask import Blueprint, request, render_template

newroutes = Blueprint("newroutes", __name__)

@newroutes.route("/books_home")
def newindex():
    print("VISITING THE NEW INDEX PAGE")
    return render_template("newhomepage.html")

@newroutes.route('/bookstoread', methods=["POST"])
def request_books_to_read():
    print("FINDING BOOKS...")
    print("FORM DATA:", dict(request.form))
    #return jsonify(request.form)

    #product_name = request.form["product_name"]
    #flash(f"Product '{product_name}' created successfully!", "success") # use the "success" category to correspond with twitter bootstrap alert colors
    #return redirect("newhomepage.html")
    return render_template("booksresults.html")
