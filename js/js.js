var announce = document.getElementsByClassName("announce")[0];
var announce_cross = document.getElementsByClassName("announce-cross")[0];
// document.getElementsByClassName("announce-text")[0].innerText = "Chaotic AUR is down Please read!";
announce_cross.style.cursor = "pointer";
announce_cross.addEventListener("click",
function(e){
    announce.setAttribute("style","bottom:-3rem;");
});
