// code to change title
if (window.location.pathname == "/"){
    document.getElementById("maintitle").innerHTML = "LOGIN"
}
else {
    document.getElementById("maintitle").innerHTML = window.location.pathname.split("/")[1].toUpperCase().replace("-", " ");
}

//code to make the x work on flash messages
var close = document.getElementsByClassName("close");
    
var i;
for (i = 0; i < close.length; i++) {
  close[i].onclick = function(){
    var div = this.parentElement;
    div.style.opacity = "0";
    setTimeout(function(){ div.style.display = "none"; });
  }
}