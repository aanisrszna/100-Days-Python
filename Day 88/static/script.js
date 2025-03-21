document.addEventListener("DOMContentLoaded", function() {
    let deleteButtons = document.querySelectorAll(".delete-btn");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function(event) {
            let confirmDelete = confirm("Are you sure you want to delete this cafe?");
            if (!confirmDelete) {
                event.preventDefault();
            }
        });
    });
});
