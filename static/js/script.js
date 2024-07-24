// Signup

document.addEventListener("DOMContentLoaded", function() {
    var urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('success')) {
        var success = urlParams.get('success');
        var message = urlParams.get('message');
        if (success === 'True') {
            showToast('Account created successfully.', 'success');
        } else if (success === 'False') {
            showToast(message ? decodeURIComponent(message) : 'Signup failed.', 'error');
        }
        window.history.replaceState({}, document.title, "{{ request.path }}");
    }
});

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

    dropdownLinks.forEach(function(link){
        link.addEventListener("click", function(event){
            event.preventDefault();
            var selectedValue = link.getAttribute("value");
            var url = baseUrl + "?selection=" + selectedValue;
            window.location.href = url;
        });
    });
});

document.addEventListener("DOMContentLoaded", function(){
    var masterNavItem = document.getElementById('master');
    var dropdownMenu = masterNavItem.querySelector('.dropdown-menu');
            
    masterNavItem.querySelector('.nav-link').addEventListener('click', function(event){
        event.preventDefault();
        dropdownMenu.style.display = dropdownMenu.style.display === 'flex' ? 'none' : 'flex';
    });

    document.addEventListener('click', function(event){
        if (!masterNavItem.contains(event.target)){
            dropdownMenu.style.display = 'none';
        }
    });
});

// Form Validation

document.addEventListener("DOMContentLoaded", function(){
    var forms = document.querySelectorAll("form.needs-validation");

    forms.forEach(function(form){
        form.addEventListener("submit", function(event){
            if(!form.checkValidity()){
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add("was-validated");
        }, false);
    });
});