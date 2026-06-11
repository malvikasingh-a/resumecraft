document.addEventListener('DOMContentLoaded', () => {
    // Handle Delete Button Click
    const deleteButtons = document.querySelectorAll('.delete-btn');

    deleteButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            if(confirm("Are you sure you want to delete this resume?")) {
                // In Django, you would perform an API call here
                // For UI demo, we just remove the card
                const cardColumn = e.target.closest('.col-md-4');
                cardColumn.remove();
            }
        });
    });
});