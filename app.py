from flask import Flask, render_template

app = Flask(__name__)

# Craftora International - 16 Premium Products Data
PRODUCTS = [
    {
        "id": 1,
        "name": "Woven Cotton Rope Storage Basket with Premium Leather Handles",
        "category": "Cotton",
        "price": "₹1799",
        "image": "cotton_storage_basket.jpg",
        "buy_link": "https://amzn.in"
    },
    {
        "id": 2,
        "name": "Premium Handmade Jute Bag / Multipurpose Basket",
        "category": "Jute",
        "price": "₹499",
        "image": "jute_bag.jpg",
        "buy_link": "https://amazon.in"
    },
    {
        "id": 3,
        "name": "Handmade Jute Coaster Set of 6 for Dining Table",
        "category": "Jute",
        "price": "₹299",
        "image": "jute_bag.jpg",
        "buy_link": "https://amazon.in"
    },
    {
        "id": 4,
        "name": "Boho Art Macrame Wall Hanging for Home Decoration",
        "category": "Decor",
        "price": "₹899",
        "image": "cotton_storage_basket.jpg",
        "buy_link": "https://amazon.in"
    },
    {
        "id": 5,
        "name": "Premium Cotton Rope Planter Basket Indoor Pot Holder",
        "category": "Cotton",
        "price": "₹649",
        "image": "cotton_storage_basket.jpg",
        "buy_link": "https://amazon.in"
    },
    {
        "id": 6,
        "name": "Handwoven Eco-Friendly Jute Table Mat",
        "category": "Jute",
        "price": "₹399",
        "image": "jute_bag.jpg",
        "buy_link": "https://amazon.in"
    },
    {
        "id": 7,
        "name": "Fancy Handmade Cotton Thread Wall Garland",
        "category": "Decor",
        "price": "₹450",
        "image": "cotton_storage_basket.jpg",
        "buy_link": "https://amazon.in"
    },
    {
        "id": 8,
        "name": "Premium Jute Laundry Basket with Cotton Lining",
        "category": "Jute",
        "price": "₹1299",
        "image": "jute_bag.jpg",
        "buy_link": "https://amazon.in"
    },
    {
        "id": 9,
        "name": "Handcrafted Cotton Rope Tissue Box Holder",
        "category": "Cotton",
        "price": "₹349",
        "image": "cotton_storage_basket.jpg",
        "buy_link": "https://amazon.in"
    },
    {
        "id": 10,
        "name": "Boho Chic Jute Rug / Floor Mat for Living Room",
        "category": "Jute",
        "price": "₹1599",
        "image": "jute_bag.jpg",
        "buy_link": "https://amazon.in"
    },
    {
        "id": 11,
        "name": "Fancy Handmade Decorative Door Hanging Toran",
        "category": "Decor",
        "price": "₹599",
        "image": "cotton_storage_basket.jpg",
        "buy_link": "https://amazon.in"
    },
    {
        "id": 12,
        "name": "Premium Cotton Macrame Cushion Cover Set",
        "category": "Cotton",
        "price": "₹799",
        "image": "cotton_storage_basket.jpg",
        "buy_link": "https://amazon.in"
    },
    {
        "id": 13,
        "name": "Handmade Jute Hanging Organizer for Kitchen",
        "category": "Jute",
        "price": "₹499",
        "image": "jute_bag.jpg",
        "buy_link": "https://amazon.in"
    },
    {
        "id": 14,
        "name": "Elegant Cotton Rope Fruit Basket for Dining Table",
        "category": "Cotton",
        "price": "₹550",
        "image": "cotton_storage_basket.jpg",
        "buy_link": "https://amazon.in"
    },
    {
        "id": 15,
        "name": "Fancy Handmade Jute Wall Clock Decor Piece",
        "category": "Jute",
        "price": "₹999",
        "image": "jute_bag.jpg",
        "buy_link": "https://amazon.in"
    },
    {
        "id": 16,
        "name": "Premium Luxury Craftora Special Decoration Item",
        "category": "Decor",
        "price": "₹2499",
        "image": "cotton_storage_basket.jpg",
        "buy_link": "https://amazon.in"
    }
]

@app.route("/")
def home():
    # Global Brand Details (Craftora International)
    owner_info = {
        "shop_name": "Craftora International",
        "name": "YUSUF HUSSAIN",
        "email": "yamaanmohd984@gmail.com",
        "phone": "+91 8630850116, 7037380116, 8791791004",
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
