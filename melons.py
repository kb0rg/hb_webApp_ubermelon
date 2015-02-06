from flask import Flask, request, session, render_template, g, redirect, url_for, flash
import model
import jinja2
import os

app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'
app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index():
    """This is the 'cover' page of the ubermelon site"""
    return render_template("index.html")

@app.route("/melons")
def list_melons():
    """This is the big page showing all the melons ubermelon has to offer"""
    melons = model.get_melons()
    return render_template("all_melons.html",
                           melon_list = melons)

@app.route("/melon/<int:id>")
def show_melon(id):
    """This page shows the details of a given melon, as well as giving an
    option to buy the melon."""
    melon = model.get_melon_by_id(id)
    print melon
    return render_template("melon_details.html",
                  display_melon = melon)

@app.route("/cart")
def shopping_cart():
    """TODO: Display the contents of the shopping cart. The shopping cart is a
    list held in the session that contains all the melons to be added. Check
    accompanying screenshots for details."""


    return render_template("cart.html")

@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    """TODO: Finish shopping cart functionality using session variables to hold
    cart list.

    Intended behavior: when a melon is added to a cart, redirect them to the
    shopping cart page, while displaying the message
    "Successfully added to cart" """

    """

    ??? where does quantity get filled in -> idea! each time the "add to cart" 
        button is clicked, increment 'qty' in session dictionary +1.
    ??? 
    """

    # thisMelon = model.get_melon_by_id(id)
    # print vars(thisMelon)
    #####

    if session.get('cart'):
            if id in session['cart']:
                print "This is the id", (id)
                session['cart'][id] += 1
                print "incremented the quantity"
            else:
                session['cart'][id] = 1
                print "This is the id", (id)
                print "added stuff to existing cart, contents are", session['cart']
    else:
        session['cart'] = {}
        session['cart'][id] = 1
        print "created a cart and added things, its contents are ", session['cart']




    return render_template("cart.html")

    #####




    # id = int(id)
    # print "ID is: ", id




    # if id in session['cart']:
    #     print "this melon is in the cart, adding to the quantity"
    #     session['cart'][id] = (session['cart'][id]) + 1
    # else:
    #     print "this melon is NOT in the cart, adding it, with qty 1"

    # session["cart"].get(id, 0)+1

    # pyCart = session['cart']

    # Here, we need to pass the melon info to the shopping_cart Python function
    # so that it can add the info to the session dictionary
    # return render_template("cart.html", jinName = thisMelon.common_name, jinPrice = thisMelon.price, jinCart = pyCart)

@app.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """TODO: Receive the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session."""
    return "Oops! This needs to be implemented"


@app.route("/checkout")
def checkout():
    """TODO: Implement a payment system. For now, just return them to the main
    melon listing page."""
    flash("Sorry! Checkout will be implemented in a future version of ubermelon.")
    return redirect("/melons")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
