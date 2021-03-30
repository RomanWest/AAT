
if (window.location.pathname == "/"){
    document.getElementById("maintitle").innerHTML = "LOGIN"
}
else {
    document.getElementById("maintitle").innerHTML = window.location.pathname.split("/")[1].toUpperCase();
}