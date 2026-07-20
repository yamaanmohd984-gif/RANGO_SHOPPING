/*=========================================
RANGO SHOPPING - WISHLIST SYSTEM
Part 1
=========================================*/

const WISHLIST_KEY = "rango_wishlist";

/* Get Wishlist */

function getWishlist() {

    return JSON.parse(localStorage.getItem(WISHLIST_KEY)) || [];

}

/* Save Wishlist */

function saveWishlist(products) {

    localStorage.setItem(
        WISHLIST_KEY,
        JSON.stringify(products)
    );

}

/* Check Product */

function isInWishlist(id) {

    return getWishlist().some(
        item => item.id === id
    );

}

/* Add Product */

function addToWishlist(product) {

    let wishlist = getWishlist();

    if (!isInWishlist(product.id)) {

        wishlist.push(product);

        saveWishlist(wishlist);

    }

}

/* Remove Product */

function removeFromWishlist(id) {

    let wishlist = getWishlist().filter(
        item => item.id !== id
    );

    saveWishlist(wishlist);

}

/* Toggle */

function toggleWishlist(product) {

    if (isInWishlist(product.id)) {

        removeFromWishlist(product.id);

    } else {

        addToWishlist(product);

    }

    updateWishlistCount();

}

/* Wishlist Counter */

function updateWishlistCount() {

    const counter = document.querySelector(".saved-count strong");

    if(counter){

        counter.innerText = getWishlist().length;

    }

}

/*=========================================
RANGO SHOPPING - WISHLIST SYSTEM
Part 2
=========================================*/

/* Heart Button Events */

function setupWishlistButtons() {

    const hearts = document.querySelectorAll(".heart-icon");

    hearts.forEach(function(button){

        const id = button.dataset.id;

        /* Page load par heart update */

        if(isInWishlist(id)){

            button.classList.add("active");

            button.innerHTML = "❤";

        }

        button.addEventListener("click", function(e){

            e.preventDefault();

            const product = {

                id: button.dataset.id,

                brand: button.dataset.brand,

                name: button.dataset.name,

                price: button.dataset.price,

                rating: button.dataset.rating,

                image: button.dataset.image,

                link: button.dataset.link

            };

            toggleWishlist(product);

            if(isInWishlist(id)){

                button.classList.add("active");

                button.innerHTML = "❤";

            }else{

                button.classList.remove("active");

                button.innerHTML = "♡";

            }

        });

    });

}

document.addEventListener("DOMContentLoaded", function(){

    setupWishlistButtons();

    updateWishlistCount();

    loadWishlistPage();

});

/*=========================================
RANGO SHOPPING - WISHLIST SYSTEM
Part 3
=========================================*/

function loadWishlistPage(){

    const grid = document.querySelector(".wishlist-grid");

    const empty = document.querySelector(".wishlist-empty");

    if(!grid) return;

    const wishlist = getWishlist();

    grid.innerHTML = "";

    if(wishlist.length === 0){

        grid.style.display = "none";

        if(empty){

            empty.style.display = "block";

        }

        return;

    }

    if(empty){

        empty.style.display = "none";

    }

    grid.style.display = "grid";

    wishlist.forEach(function(product){

        grid.innerHTML += `

<div class="wishlist-card">

<div class="heart">❤</div>

<img src="${product.image}" alt="${product.name}">

<div class="card-body">

<div class="brand">

${product.brand}

</div>

<div class="title">

${product.name}

</div>

<div class="rating">

⭐ ${product.rating}

</div>

<div class="price">

${product.price}

</div>

<a href="${product.link}"

target="_blank"

class="buy-btn">

Buy On Official Site

</a>

<button

class="remove-btn"

onclick="deleteWishlistProduct('${product.id}')">

Remove

</button>

</div>

</div>

`;

    });

}


/*=========================================
RANGO SHOPPING - WISHLIST SYSTEM
Part 4 (Final)
=========================================*/

/* Remove Single Product */

function deleteWishlistProduct(id){

    removeFromWishlist(id);

    updateWishlistCount();

    loadWishlistPage();

    setupWishlistButtons();

}

/* Clear Wishlist */

function clearWishlist(){

    if(confirm("Are you sure you want to clear your Wishlist?")){

        localStorage.removeItem(WISHLIST_KEY);

        updateWishlistCount();

        loadWishlistPage();

        setupWishlistButtons();

    }

}

/* Clear Button */

document.addEventListener("DOMContentLoaded", function(){

    const clearBtn=document.querySelector(".clear-btn");

    if(clearBtn){

        clearBtn.addEventListener("click",function(e){

            e.preventDefault();

            clearWishlist();

        });

    }

});

/* Heart Color Update */

function refreshHearts(){

    document.querySelectorAll(".heart-icon").forEach(function(btn){

        if(isInWishlist(btn.dataset.id)){

            btn.classList.add("active");

            btn.innerHTML="❤";

        }

        else{

            btn.classList.remove("active");

            btn.innerHTML="♡";

        }

    });

}

/* Page Refresh */

window.addEventListener("storage",function(){

    updateWishlistCount();

    loadWishlistPage();

    refreshHearts();

});

/* First Load */

document.addEventListener("DOMContentLoaded",function(){

    updateWishlistCount();

    loadWishlistPage();

    refreshHearts();

});

/* AUTO PRODUCT DETECTION */

document.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll(".product-card").forEach((card, index) => {

        let heart = card.querySelector(".heart-icon");

        if (!heart) {
            heart = document.createElement("button");
            heart.className = "heart-icon";
            heart.innerHTML = "♡";
            card.prepend(heart);
        }

        const img = card.querySelector("img");
        const title = card.querySelector("h3");
        const brand = card.querySelector(".brand");
        const price = card.querySelector(".price");
        const rating = card.querySelector(".rating");
        const link = card.querySelector("a");

        heart.dataset.id = "product_" + index;
        heart.dataset.name = title ? title.innerText : "";
        heart.dataset.brand = brand ? brand.innerText : "";
        heart.dataset.price = price ? price.innerText : "";
        heart.dataset.rating = rating ? rating.innerText : "";
        heart.dataset.image = img ? img.src : "";
        heart.dataset.link = link ? link.href : "#";
    });

    setupWishlistButtons();
});

/*=========================================
END
=========================================*/