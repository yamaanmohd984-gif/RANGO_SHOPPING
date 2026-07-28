import os
import sqlite3

# --- फ़ोल्डर स्ट्रक्चर के हिसाब से सही पाथ (इसे अपडेट किया है) ---
# यह बिना किसी एरर के ठीक इसी फ़ोल्डर (static/database) के अंदर rango.db बनाएगा
DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rango.db")
# -----------------------------------------------------------

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
category TEXT NOT NULL,
price TEXT,
image TEXT,
description TEXT,
affiliate_link TEXT
)
""")

# Contact messages table
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
message TEXT
)
""")

# Sample products
products = [
    (
        "Luxury Sneakers",
        "Men",
        "₹3999",
        "men_shoes.jpg",
        "Premium luxury footwear",
        "#"
    ),
    (
        "Designer Dress",
        "Women",
        "₹4999",
        "women_dress.jpg",
        "Elegant fashion collection",
        "#"
    ),
    (
        "Kids Premium Wear",
        "Kids",
        "₹1999",
        "kids_clothes.jpg",
        "Comfortable kids fashion",
        "#"
    )
]

cursor.executemany("""
INSERT INTO products
(name,category,price,image,description,affiliate_link)
VALUES (?,?,?,?,?,?)
""", products)

conn.commit()
conn.close()

print("Rango Shopping Database Created Successfully")
