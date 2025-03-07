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
    var taskSearchInput = document.getElementById("task-search");

    if(companySearchInput){
        companySearchInput.addEventListener("input", function(){
            searchTable('company-search', 'company-name-table');
        });
    }

    if(taskSearchInput){
        taskSearchInput.addEventListener("input", function(){
            searchTable('task-search', 'task-name-table');
        });
    }

    function searchTable(inputId, tableId) {
        var input, filter, table, tr, td, i, txtValue, txtValueAssigned;
        input = document.getElementById(inputId);
        filter = input.value.toLowerCase();
        table = document.getElementById(tableId);
        tr = table.getElementsByTagName("tr");

        // Loop through all table rows and search in both Title and Assigned To
        for (i = 1; i < tr.length; i++) {
            tdTitle = tr[i].getElementsByTagName("td")[0]; // Task title is in the first column
            tdAssigned = tr[i].getElementsByTagName("td")[1]; // Assigned to is in the second column
            if (tdTitle || tdAssigned) {
                txtValueTitle = tdTitle.textContent || tdTitle.innerText;
                txtValueAssigned = tdAssigned.textContent || tdAssigned.innerText;
                if (txtValueTitle.toLowerCase().indexOf(filter) > -1 || txtValueAssigned.toLowerCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
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

// Form Double Submission Avoidance
if( window.history.replaceState ){
    window.history.replaceState( null, null, window.location.href );
}