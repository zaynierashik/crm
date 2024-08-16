// Password Toggle
function toggleSignupPasswordVisibility() {
    const passwordField = document.getElementById('password');
    const checkbox = document.getElementById('checkbox');
    if (checkbox.checked) {
        passwordField.type = 'text';
    } else {
        passwordField.type = 'password';
    }
}

function toggleLoginPasswordVisibility() {
    const passwordField = document.getElementById('login-password');
    const checkbox = document.getElementById('login-checkbox');
    if (checkbox.checked) {
        passwordField.type = 'text';
    } else {
        passwordField.type = 'password';
    }
}

// Company & Partner Search
function searchTable(inputId, tableId){
    var input, filter, table, tr, td, i, txtValue;
    
    input = document.getElementById(inputId);
    filter = input.value.toUpperCase();
    table = document.getElementById(tableId);
    tr = table.getElementsByTagName("tr");

    for(i = 0; i < tr.length; i++){
        td = tr[i].getElementsByTagName("td")[0];
        if(td){
            txtValue = td.textContent || td.innerText;
            if(txtValue.toUpperCase().indexOf(filter) > -1){
                tr[i].style.display = "";
            }else{
                tr[i].style.display = "none";
            }
        }
    }
}

document.addEventListener("DOMContentLoaded", function(){
    var companySearchInput = document.getElementById("company-search");
    var partnerSearchInput = document.getElementById("partner-search");

    if(companySearchInput){
        companySearchInput.addEventListener("input", function(){
            searchTable('company-search', 'company-name-table');
        });
    }

    if(partnerSearchInput){
        partnerSearchInput.addEventListener("input", function(){
            searchTable('partner-search', 'partner-name-table');
        });
    }
});

// City Filter
document.getElementById('city-filter').addEventListener('change', function(){
    var selectedCity = this.value;
    var url = new URL(window.location.href);
    if (selectedCity){
        url.searchParams.set('city', selectedCity);
    } else{
        url.searchParams.delete('city');
    }
    window.location.href = url.toString();
});

// Toggle Via Fields
var viaDropdown = document.getElementById("via");
var referralDiv = document.getElementById("referralDiv");
var partnerDiv = document.getElementById("partnerDiv");

viaDropdown.addEventListener("change", function(){
    var selectedVia = viaDropdown.value;
    if(selectedVia === "Referral"){
        referralDiv.style.display = "block";
        partnerDiv.style.display = "none";
    }else if(selectedVia === "Partner"){
        referralDiv.style.display = "none";
        partnerDiv.style.display = "block";
    }else{
        referralDiv.style.display = "none";
        partnerDiv.style.display = "none";
    }
});

// Clone Contact Form
document.addEventListener('DOMContentLoaded', () => {
    const addContactBtn = document.getElementById('add-contact-btn');
    const contactsContainer = document.getElementById('contacts-container');

    addContactBtn.addEventListener('click', () => {
        const newContactForm = contactsContainer.querySelector('.contact-form').cloneNode(true);
        
        const newContactFormContainer = document.createElement('div');
        newContactFormContainer.classList.add('px-4', 'py-5', 'mb-8', 'bg-white', 'rounded-lg', 'shadow-md', 'dark:bg-gray-800');
        newContactFormContainer.appendChild(newContactForm);
        
        contactsContainer.parentElement.insertBefore(newContactFormContainer, contactsContainer.nextSibling);
    });
});

// Form Double Submission Avoidance
if( window.history.replaceState ){
    window.history.replaceState( null, null, window.location.href );
}