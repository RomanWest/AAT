// code to change title
if (window.location.pathname == "/") {
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
  close[i].onclick = function () {
    var div = this.parentElement;
    div.style.opacity = "0";
    setTimeout(function () { div.style.display = "none"; });
  }
}

//code to hide the home button if user is not logged in and on the login page

if (window.location.pathname == "/login" || window.location.pathname == "/") {
  document.getElementById("homebtn").style.display = "none";
}


//code to replace left margin with sidebar on student home
//i changed == to includes so that itll work when we add additional routes after e.g student-home/stats
if (window.location.pathname.includes("/Student-Home")) {
  document.getElementsById("content").style.marginLeft = "0";
}
else {
  document.getElementById("content").style.marginLeft = "10%";
}

//function to change url based on dropdown menu

function dropdownURL() {
  if (document.getElementById("qType").value = "Fill in the Blank") {
    var newurl = window.location.href.replace(window.location.pathname, "/Create-Fill-in-the-Blank");
    location.replace(newurl)
  }
}

function dropdownURL2() {
  if (document.getElementById("qType").value = "Multiple Choice") {
    var newurl = window.location.href.replace(window.location.pathname, "/Create-Multiple-Choice-Question");
    location.replace(newurl)
  }
}

//counter for ticks
function questionCheck() {
  var count = 0;
  var noElements = document.getElementsByClassName("checkbx");
  for (var i = 0; i < noElements.length; i++) {
    count += 1;
    if (noElements[i].checked == false) {
      count -= 1
      noElements[i].name = "unchecked";
    }
    if (noElements[i].checked == true) {
      noElements[i].name = "checked!";
    }
  }
  console.log(count);
  document.getElementById("question-counter").innerText = count + "/ 3";

}

function uncheck() {
  var noElements = document.getElementsByClassName("checkbx");
  for (var i = 0; i < noElements.length; i++) {
    noElements[i].checked = false;
  }
}

function filter() {
  var filterType = document.getElementById("assessmentDropdown");
  var question_type = document.getElementsByClassName("question-type");
  var question = document.getElementsByClassName("assessment-question");
  var filterModule = document.getElementById("moduleDropdown");
  var moduleCode = document.getElementsByClassName("module-code");

  var Type = document.getElementsByClassName("hiddenType");
  var Module = document.getElementsByClassName("hiddenModule");

  for (i = 0; i < filterModule.length-1; i ++) {
    if (filterModule[i].value == filterModule[i+1].value){
      filterModule[i].style.display = 'none';
    }
  }

  for (i = 0; i < Type.length; i ++){
    if (Type[i].id == filterType.value){
      Type[i].name = "selectedType";
    } else {
      Type[i].name = Type[i].id;
    }
  }

  for (i = 0; i < Module.length; i ++){
    if (Module[i].id == filterModule.value){
      Module[i].name = "selectedModule";
    } else {
      Module[i].name = Module[i].id;
    }
  }

  for (i = 0; i < question.length; i++) {
    // Filter on both Question Type and Module Code
    if (question_type[i].innerHTML == filterType.value && moduleCode[i].innerHTML == filterModule.value) {
      question[i].style.display = "block";
    } // Filter on just Module Code
    else if (filterType.value == 'Select Type' && moduleCode[i].innerHTML == filterModule.value) {
      question[i].style.display = "block";
    } //Filter on just Question Type
    else if (filterModule.value == 'Select Module' && question_type[i].innerHTML == filterType.value) {
      question[i].style.display = "block";
    } // No Filter
    else if (filterModule.value == 'Select Module' && filterType.value == 'Select Type') {
      question[i].style.display = "block";
    } // Does not match
    else {
      question[i].style.display = "none";
    }
  }
}