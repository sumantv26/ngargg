var mybutton = document.querySelector("#f-btn");
mybutton.style.color = "blue"

window.onscroll = function() { scrollFunction() };

function scrollFunction() {
    if (document.body.scrollTop > 30 || document.documentElement.scrollTop > 30) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

function scrollPageToTop() {
    console.log("clicked")
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}