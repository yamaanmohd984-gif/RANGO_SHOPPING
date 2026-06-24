from flask import Flask, render_template

app = Flask(__name__)

# Craftora International Premium Products Data
PRODUCTS = [
    {
        "id": 1,
        "name": "Woven Cotton Rope Storage Basket with Premium Leather Handles",
        "category": "Cotton",
        "price": "₹1799",
        "image": "cotton_storage_basket.jpg", # <-- Humne naam chota aur sahi kar diya hai
        "buy_link": "https://amzn.in"
    },
    {
        "id": 2,
        "name": "Premium Handmade Jute Bag / Multipurpose Basket",
        "category": "Jute",
        "price": "₹499",
        "image": "jute_bag.jpg",
        "buy_link": "https://amazon.in"
    }
]

@app.route("/")
def home():
    # 🤝 Global Brand Details (Craftora International)
    owner_info = {
        "shop_name": "Craftora International",
        "name": "YUSUF HUSSAIN",
        "email": "yamaanmohd984@gmail.com", # <-- Aapki asli email jodi hai
        "phone": "+91 8630850116, 7037380116, 8791791004", # <-- Teeno numbers jode hain
        "about": (
            "Welcome to Craftora International! We take immense pride in crafting 100% pure "
            "handmade premium products designed to bring warmth and elegance to modern homes worldwide. "
            "From beautifully woven eco-friendly Jute Coasters and exquisite Storage Baskets 🧺 "
            "to a wide range of fancy home decoration items, every piece is carefully crafted "
            "by hand with maximum attention to quality and durability. We believe in sustainable "
            "creativity, ensuring that our products are not only stunning to look at but also safe "
            "for the environment. Thank you for supporting authentic handmade craftsmanship—we promise "
            "premium quality and global trust in every thread!"
        )
    }
    return render_template("shop.html", products=PRODUCTS, owner=owner_info)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
