let navbar = document.querySelector('.header .flex .navbar');

document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active');
}

window.onscroll = () =>{
    navbar.classList.remove('active');
}

document/querySelectorAll('input[type-"number"]').forEach(inputNumber =>{
    if(inputNumber.value.length > inputNumber.maxLength) inputNumber.value 
    = inputNumber.value.slice(0, inputNumber.maxLength);
    
});

document.addEventListener('DOMContentLoaded', function() {
    // Dropdown functionality
    let dropdown_items = document.querySelectorAll('.job-filter form .dropdown-container .dropdown .lists .items');
    
    dropdown_items.forEach(item => {
        item.addEventListener('click', function() {
            const parentDropdown = this.closest('.dropdown');
            const output = parentDropdown.querySelector('.output');
            output.value = this.innerText;
        });
    });
    
    // Toggle dropdown visibility
    const dropdownOutputs = document.querySelectorAll('.dropdown .output');
    dropdownOutputs.forEach(output => {
        output.addEventListener('click', function() {
            const parentDropdown = this.closest('.dropdown');
            const lists = parentDropdown.querySelector('.lists');
            lists.style.display = lists.style.display === 'block' ? 'none' : 'block';
            
            // Close other open dropdowns
            document.querySelectorAll('.dropdown .lists').forEach(list => {
                if (list !== lists) {
                    list.style.display = 'none';
                }
            });
        });
    });
    
    // Close dropdowns when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.dropdown')) {
            document.querySelectorAll('.dropdown .lists').forEach(list => {
                list.style.display = 'none';
            });
        }
    });
    
    // Save job functionality
    const saveButtons = document.querySelectorAll('.save-btn');
    saveButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const jobId = this.getAttribute('data-job-id');
            this.classList.toggle('fas');
            this.classList.toggle('far');
            
            // Here you would typically send an AJAX request to save the job
            fetch('/save-job', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': '{{ csrf_token() }}'
                },
                body: JSON.stringify({ job_id: jobId })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Optional: Show a success message
                }
            });
        });
    });
});



















































