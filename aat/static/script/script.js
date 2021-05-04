// code to change title
if (window.location.pathname == "/"){
    document.getElementById("maintitle").innerHTML = "LOGIN"
}

//IMPORTANT
// as long as all the names of the routes are in the format student-home or staff-home, the main title will be correct
else {
    document.getElementById("maintitle").innerHTML = window.location.pathname.split("/")[1].toUpperCase().replace(/-/g, " ");
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

//code to hide the home button if user is not logged in and on the login page

if (window.location.pathname == "/login" || window.location.pathname == "/"){
 document.getElementById("homebtn").style.display= "none";
}


//code to replace left margin with sidebar on student home
//i changed == to includes so that itll work when we add additional routes after e.g student-home/stats
if (window.location.pathname.includes("/Student-Home")){
  document.getElementsById("content").style.marginLeft= "0";
}
else{
  document.getElementById("content").style.marginLeft= "10%";
}

