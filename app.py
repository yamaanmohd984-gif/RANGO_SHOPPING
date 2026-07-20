from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)


DATABASE = "database/rango.db"



# Database connection

def get_db_connection():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn




# Home Page

@app.route("/")
def home():

    conn = get_db_connection()

    products = conn.execute(
        "SELECT * FROM products LIMIT 6"
    ).fetchall()

    conn.close()


    return render_template(
        "index.html",
        products=products
    )




# Men Category

@app.route("/men")
def men():

    conn = get_db_connection()

    products = conn.execute(
        "SELECT * FROM products WHERE category='Men'"
    ).fetchall()

    conn.close()


    return render_template(
        "men.html",
        products=products
    )




# Women Category

@app.route("/women")
def women():

    conn = get_db_connection()

    products = conn.execute(
        "SELECT * FROM products WHERE category='Women'"
    ).fetchall()

    conn.close()


    return render_template(
        "women.html",
        products=products
    )




# Kids Category

@app.route("/kids")
def kids():

    conn = get_db_connection()

    products = conn.execute(
        "SELECT * FROM products WHERE category='Kids'"
    ).fetchall()

    conn.close()


    return render_template(
        "kids.html",
        products=products
    )




# Product Page

@app.route("/product/<int:id>")
def product(id):

    conn = get_db_connection()

    product = conn.execute(
        "SELECT * FROM products WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()


    return render_template(
        "product.html",
        product=product
    )




# Search

@app.route("/search")
def search():

    query = request.args.get("query", "").strip()

    if query == "":
        return render_template(
            "search.html",
            products=[],
            query=""
        )

    conn = get_db_connection()

    products = conn.execute(
        "SELECT * FROM products WHERE name LIKE ?",
        ('%' + query + '%',)
    ).fetchall()

    conn.close()

    return render_template(
        "search.html",
        products=products,
        query=query
    )


# Wishlist

@app.route("/wishlist")
def wishlist():

    return render_template("wishlist.html")




# Offers

@app.route("/offers")
def offers():

    return render_template("offers.html")




# About

@app.route("/about")
def about():

    return render_template("about.html")




# Contact

@app.route("/contact")
def contact():

    return render_template("contact.html")




# Privacy

@app.route("/privacy")
def privacy():

    return render_template("privacy.html")


# =========================
# MEN CATEGORY PAGES
# =========================

@app.route("/Men-fashion")
def Men_fashion():
    return render_template("Men's-fashion.html")


@app.route("/lower-fashion")
def lower_fashion():
    return render_template("lower-fashion.html")


@app.route("/tshirts")
def tshirts():
    return render_template("tshirts.html")


@app.route("/shirts")
def shirts():
    return render_template("shirts.html")


@app.route("/jeans")
def jeans():
    return render_template("jeans.html")


@app.route("/jackets")
def jackets():
    return render_template("jackets.html")


@app.route("/shoes")
def shoes():
    return render_template("shoes.html")


@app.route("/watches")
def watches():
    return render_template("watches.html")


@app.route("/wallet-belts")
def wallet_belts():
    return render_template("wallet-belts.html")


@app.route("/perfumes")
def perfumes():
    return render_template("perfumes.html")


@app.route("/sunglasses")
def sunglasses():
    return render_template("sunglasses.html")


@app.route("/jewellery")
def jewellery():
    return render_template("jewellery.html")


# =========================
# WOMEN CATEGORY ROUTES
# =========================

@app.route("/w-dresses")
def w_dresses():
    return render_template("w-dresses.html")


@app.route("/w-tops")
def w_tops():
    return render_template("w-tops.html")


@app.route("/w-tshirts")
def w_tshirts():
    return render_template("w-tshirts.html")


@app.route("/w-shirts")
def w_shirts():
    return render_template("w-shirts.html")


@app.route("/w-jeans")
def w_jeans():
    return render_template("w-jeans.html")


@app.route("/w-jackets")
def w_jackets():
    return render_template("w-jackets.html")


@app.route("/w-heels")
def w_heels():
    return render_template("w-heels.html")


@app.route("/w-handbags")
def w_handbags():
    return render_template("w-handbags.html")


@app.route("/w-watches")
def w_watches():
    return render_template("w-watches.html")


@app.route("/w-jewellery")
def w_jewellery():
    return render_template("w-jewellery.html")


@app.route("/w-perfumes")
def w_perfumes():
    return render_template("w-perfumes.html")


@app.route("/w-sunglasses")
def w_sunglasses():
    return render_template("w-sunglasses.html")



# =========================
# KIDS CATEGORY ROUTES
# =========================

@app.route("/kids-tshirts")
def kids_tshirts():
    return render_template("kids-tshirts.html")


@app.route("/kids-shirts")
def kids_shirts():
    return render_template("kids-shirts.html")


@app.route("/kids-jeans")
def kids_jeans():
    return render_template("kids-jeans.html")


@app.route("/kids-jackets")
def kids_jackets():
    return render_template("kids-jackets.html")


@app.route("/kids-shoes")
def kids_shoes():
    return render_template("kids-shoes.html")


@app.route("/kids-watches")
def kids_watches():
    return render_template("kids-watches.html")


@app.route("/kids-backpacks")
def kids_backpacks():
    return render_template("kids-backpacks.html")


@app.route("/kids-toys")
def kids_toys():
    return render_template("kids-toys.html")


@app.route("/kids-accessories")
def kids_accessories():
    return render_template("kids-accessories.html")


@app.route("/kids-sunglasses")
def kids_sunglasses():
    return render_template("kids-sunglasses.html")


# Terms

@app.route("/terms")
def terms():

    return render_template("terms.html")




# 404

@app.errorhandler(404)

def page_not_found(error):

    return render_template("404.html"),404




if __name__ == "__main__":

    app.run(debug=True)