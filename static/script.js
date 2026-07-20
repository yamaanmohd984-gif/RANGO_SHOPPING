// =================================
// RANGO SHOPPING JAVASCRIPT
// =================================


// Mobile menu future support

document.addEventListener("DOMContentLoaded", function(){

    console.log("Rango Shopping Loaded Successfully");

});



// Wishlist button animation

function addWishlist(){

    alert("Product added to your wishlist!");

}



// Smooth scrolling

document.querySelectorAll('a[href^="#"]').forEach(anchor => {

    anchor.addEventListener("click", function(e){

        e.preventDefault();

        document.querySelector(this.getAttribute("href"))
        .scrollIntoView({

            behavior:"smooth"

        });

    });

});