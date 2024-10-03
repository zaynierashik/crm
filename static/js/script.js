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

// User Login Error
function showErrorToast(message) {
    const toastContainer = document.getElementById('toast-container');
    const toastTemplate = document.getElementById('error-toast-template').cloneNode(true);
    toastTemplate.classList.remove('hidden');
    toastTemplate.querySelector('#toast-message').textContent = message;

    toastContainer.appendChild(toastTemplate);

    setTimeout(() => {
        hideToast(toastTemplate);
    }, 3000);
}

function hideToast(toastElement) {
    toastElement.remove();
}

// Trigger an error toast if there's an error message passed from the backend
window.onload = function() {
    const urlParams = new URLSearchParams(window.location.search);
    const errorMessage = urlParams.get('error_message');
    if (errorMessage) {
        showErrorToast(errorMessage);

        // Clean the URL by removing the error message after it's displayed
        window.history.replaceState({}, document.title, window.location.pathname);
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

// AJAX Submission
document.addEventListener("DOMContentLoaded", function(){
    function handleFormSubmission(formId, dropdownId, modalId, responseKey){
        var form = document.getElementById(formId);
        if(form.checkValidity()){
            var formData = new FormData(form);
            var xhr = new XMLHttpRequest();
                    
            xhr.onreadystatechange = function(){
                if(xhr.readyState == XMLHttpRequest.DONE){
                    if(xhr.status == 200){
                        var response = JSON.parse(xhr.responseText);
                        var dropdown = document.getElementById(dropdownId);
                        var options = dropdown.options;
                        var exists = false;

                        for(var i = 0; i < options.length; i++){
                            if(options[i].value === response[responseKey]){
                                exists = true;
                                break;
                            }
                        }

                        if(!exists){
                            var option = document.createElement("option");
                            option.text = response[responseKey];
                            option.value = response[responseKey];
                            dropdown.add(option);
                        }
                                
                        $(modalId).modal('hide');
                    } else if(xhr.status == 400){
                        var response = JSON.parse(xhr.responseText);
                        alert(response.error);
                    } else {
                        console.error('Error:', xhr.statusText);
                    }
                }
            };

            xhr.open("POST", form.action);
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
            xhr.send(formData);
        }else{
            form.classList.add("was-validated");
        }
    }

    document.getElementById("ajax-sector-button").addEventListener("click", function(){
        handleFormSubmission("sectorForm", "sector", "crud-modal", "sector_name");
    });
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

// Form Double Submission Avoidance
if( window.history.replaceState ){
    window.history.replaceState( null, null, window.location.href );
}