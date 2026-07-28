from flask import Flask, render_template, request, make_response
import sqlite3
import os  # <-- यह नया इम्पोर्ट जोड़ा है

app = Flask(__name__)

# --- डेटाबेस का सही और डायनामिक पाथ (इसे बदल दिया है) ---
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(BASE_DIR, "static", "database", "rango.db") 
# ----------------------------------------------------

# Database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Home Page
@app.route("/")
def home():
    conn = get_db_connection()
    # यहाँ एरर आ रही थी क्योंकि डेटाबेस फ़ाइल सर्वर को मिल नहीं रही थी
    products = conn.execute("SELECT * FROM products LIMIT 6").fetchall()
    conn.close()
    return render_template("index.html", products=products)

# Men Category
@app.route("/men")
def men():
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products WHERE category='Men'").fetchall()
    conn.close()
    return render_template("men.html", products=products)

# Women Category
@app.route("/women")
def women():
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products WHERE category='Women'").fetchall()
    conn.close()
    return render_template("women.html", products=products)

# Kids Category
@app.route("/kids")
def kids():
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products WHERE category='Kids'").fetchall()
    conn.close()
    return render_template("kids.html", products=products)

# Product Detail Page
@app.route("/product/<int:id>")
def product(id):
    conn = get_db_connection()
    product = conn.execute("SELECT * FROM products WHERE id=?", (id,)).fetchone()
    conn.close()
    return render_template("product.html", product=product)

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

# Terms
@app.route("/terms")
def terms():
    return render_template("terms.html")

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

# Dynamic XML Sitemap for Google Search Console
@app.route("/sitemap.xml")
def sitemap():
    host = request.host_url
    static_urls = [
        "", "men", "women", "kids", "offers", "wishlist", "about", "contact", "privacy", "terms",
        "Men-fashion", "lower-fashion", "tshirts", "shirts", "jeans", "jackets", "shoes", "watches", 
        "wallet-belts", "perfumes", "sunglasses", "jewellery", "w-dresses", "w-tops", "w-tshirts", 
        "w-shirts", "w-jeans", "w-jackets", "w-heels", "w-handbags", "w-watches", "w-jewellery", 
        "w-perfumes", "w-sunglasses", "kids-tshirts", "kids-shirts", "kids-jeans", "kids-jackets", 
        "kids-shoes", "kids-watches", "kids-backpacks", "kids-toys", "kids-accessories", "kids-sunglasses"
    ]
    
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://sitemaps.org">\n'
    
    for url in static_urls:
        xml_content += f"  <url>\n    <loc>{host}{url}</loc>\n    <changefreq>daily</changefreq>\n    <priority>0.7</priority>\n  </url>\n"
        
    xml_content += "</urlset>"
    response = make_response(xml_content)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/robots.txt')
def robots_txt():
    host = request.host_url
    return f"User-agent: *\nAllow: /\nSitemap: {host}sitemap.xml"

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
