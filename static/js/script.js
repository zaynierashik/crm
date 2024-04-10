// Back to Top

function toggleTopContainerVisibility(){
    const topContainer = document.getElementById('top');
    if(window.scrollY >= 750){
        topContainer.classList.add('show');
    }else{
        topContainer.classList.remove('show');
    }
}

window.addEventListener('scroll', toggleTopContainerVisibility);

document.getElementById('scroll-to-top').addEventListener('click', function (event){
    event.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
});

toggleTopContainerVisibility();

// Show Password

function showPassword(){
    var x = document.getElementById("password");
    if(x.type == "password"){
        x.type = "text";
    }else{
        x.type = "password";
    }
}