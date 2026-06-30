from flask import Flask, render_template

app = Flask(__name__)

SHOE_CATEGORIES = [
    "Sneakers", "Casual", "Sports", "Formal", 
    "Boots", "Loafers", "Luxury", "Running"
]

LUXURY_SHOES = [
    {"id": 1, "brand": "Balenciaga", "name": "Triple S Black", "cat": "Sneakers", "price": "₹85,000", "url": "https://balenciaga.com"},
    {"id": 2, "brand": "Gucci", "name": "Ace Leather Sneaker", "cat": "Luxury", "price": "₹72,000", "url": "https://gucci.com"},
    {"id": 3, "brand": "Louis Vuitton", "name": "LV Trainer", "cat": "Sneakers", "price": "₹1,10,000", "url": "https://louisvuitton.com"},
    {"id": 4, "brand": "Prada", "name": "Cloudbust Thunder", "cat": "Sports", "price": "₹95,000", "url": "https://prada.com"},
    {"id": 5, "brand": "Christian Louboutin", "name": "Louis Orlato", "cat": "Luxury", "price": "₹88,000", "url": "https://christianlouboutin.com"},
    {"id": 6, "brand": "Nike", "name": "Air Jordan 1 Retro", "cat": "Sneakers", "price": "₹1,50,000", "url": "https://nike.com"},
    {"id": 7, "brand": "Adidas Y-3", "name": "Runner 4D", "cat": "Running", "price": "₹42,000", "url": "https://adidas.com"},
    {"id": 8, "brand": "Tom Ford", "name": "Elkan Leather Oxford", "cat": "Formal", "price": "₹1,25,000", "url": "https://tomford.com"},
    {"id": 9, "brand": "Hermès", "name": "Bouncing Sneaker", "cat": "Casual", "price": "₹78,000", "url": "https://hermes.com"},
    {"id": 10, "brand": "Salvatore Ferragamo", "name": "Gancini Loafers", "cat": "Loafers", "price": "₹65,000", "url": "https://ferragamo.com"},
    {"id": 11, "brand": "Versace", "name": "Chain Reaction", "cat": "Sports", "price": "₹82,000", "url": "https://versace.com"},
    {"id": 12, "brand": "Saint Laurent", "name": "Wyatt Chelsea Boots", "cat": "Boots", "price": "₹98,000", "url": "https://ysl.com"},
    {"id": 13, "brand": "Alexander McQueen", "name": "Oversized Runner", "cat": "Casual", "price": "₹55,000", "url": "https://alexandermcqueen.com"},
    {"id": 14, "brand": "Bottega Veneta", "name": "The Lug Boot", "cat": "Boots", "price": "₹1,15,000", "url": "https://bottegaveneta.com"},
    {"id": 15, "brand": "Burberry", "name": "Regis Vintage Check", "cat": "Casual", "price": "₹58,000", "url": "https://burberry.com"},
    {"id": 16, "brand": "Valentino", "name": "Rockstud Untitled", "cat": "Sneakers", "price": "₹68,000", "url": "https://valentino.com"},
    {"id": 17, "brand": "Dior", "name": "B23 High-Top", "cat": "Luxury", "price": "₹1,05,000", "url": "https://dior.com"},
    {"id": 18, "brand": "Givenchy", "name": "Spectre Runner", "cat": "Running", "price": "₹74,000", "url": "https://givenchy.com"},
    {"id": 19, "brand": "Fendi", "name": "Flow Neoprene", "cat": "Sports", "price": "₹80,000", "url": "https://fendi.com"},
    {"id": 20, "brand": "Balmain", "name": "B-Court Leather", "cat": "Formal", "price": "₹62,000", "url": "https://balmain.com"}
]

@app.route('/')
def home():
    featured_shoes = LUXURY_SHOES[:6]
    return render_template('index.html', shoes=featured_shoes, categories=SHOE_CATEGORIES, site_name="Luxury Footwear")

@app.route('/category')
def category():
    return render_template('category.html', shoes=LUXURY_SHOES, categories=SHOE_CATEGORIES, site_name="Luxury Footwear")

if __name__ == '__main__':
    app.run(debug=True)