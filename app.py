from flask import Flask, render_template

app = Flask(__name__)

SHOE_CATEGORIES = [
    "Sneakers", "Casual", "Sports", "Formal",
    "Boots", "Loafers", "Luxury", "Running"
]

LUXURY_SHOES = [
    {"id": 1, "brand": "Puma", "url": "https://puma.com"},
    {"id": 2, "brand": "Gucci", "url": "https://gucci.com"},
    {"id": 3, "brand": "Louis Vuitton", "url": "https://louisvuitton.com"},
    {"id": 4, "brand": "Prada","url": "https://prada.com"},
    {"id": 5, "brand": "Christian Louboutin",  "url": "https://christianlouboutin.com"},
    {"id": 6, "brand": "Nike","url": "https://nike.com"},
    {"id": 7, "brand": "Adidas Y-3",  "url": "https://adidas.com"},
    {"id": 8, "brand": "Tom Ford",  "url": "https://tomford.com"},
    {"id": 9, "brand": "Hermès", "url": "https://hermes.com"},
    {"id": 10, "brand": "Salvatore Ferragamo", "url": "https://ferragamo.com"},
    {"id": 11, "brand": "Versace", "url": "https://versace.com"},
    {"id": 12, "brand": "Saint Laurent", "url": "https://ysl.com"},
    {"id": 13, "brand": "Alexander McQueen",  "url": "https://alexandermcqueen.com"},
    {"id": 14, "brand": "Bottega Veneta", "url": "https://bottegaveneta.com"},
    {"id": 15, "brand": "Burberry","url": "https://burberry.com"},
    {"id": 16, "brand": "Valentino", "url": "https://valentino.com"},
    {"id": 17, "brand": "Dior", "url": "https://dior.com"},
    {"id": 18, "brand": "Givenchy",  "url": "https://givenchy.com"},
    {"id": 19, "brand": "Fendi", "url": "https://fendi.com"},
    {"id": 20, "brand": "Balmain", "url": "https://balmain.com"}
]

@app.route('/')
def home():
    featured_shoes = LUXURY_SHOES[:6]
    return render_template('index.html', shoes=featured_shoes, categories=SHOE_CATEGORIES, site_name="Luxury Footwear")

@app.route('/category')
def category():
    return render_template('category.html', shoes=LUXURY_SHOES, categories=SHOE_CATEGORIES, site_name="Luxury Footwear")

if __name__ == '__main__':
    import os
    port = int(os.environ.get("port", 5000))
    app.run(host='0.0.0.0', port=port)
    
