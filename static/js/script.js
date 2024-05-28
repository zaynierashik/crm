// Show Password

function showPassword(){
    var x = document.getElementById("password");
    if(x.type == "password"){
        x.type = "text";
    }else{
        x.type = "password";
    }
}

function showLoginPassword(){
    var x = document.getElementById("loginpassword");
    if(x.type == "password"){
        x.type = "text";
    }else{
        x.type = "password";
    }
}

// Dropdown Menu

document.addEventListener("DOMContentLoaded", function(){
    var baseUrl = "/master/";
    var dropdownLinks = document.querySelectorAll("#master .dropdown-item");

    dropdownLinks.forEach(function(link) {
        link.addEventListener("click", function(event) {
            event.preventDefault();
            var selectedValue = link.getAttribute("value");
            var url = baseUrl + "?selection=" + selectedValue;
            window.location.href = url;
        });
    });
});