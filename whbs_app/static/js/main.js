
        const searchBox = document.getElementById('search-box');
        const searchButton = document.getElementById('search-button');
        const hallCards = document.querySelectorAll('.hall-card');
        // const noResultsMessage = document.getElementById('no-results');

        function performSearch() {
            const searchTerm = searchBox.value.toLowerCase();
            let resultsFound = false;

            hallCards.forEach(card => {
                const hallName = card.dataset.name;
                

                if (hallName.includes(searchTerm) ) {
                    card.style.display = 'block';
                    resultsFound = true;
                } else {
                    card.style.display = 'none';
                }
            });

            
        }

        searchButton.addEventListener('click', performSearch);
        searchBox.addEventListener('keyup', function(event) {
            if (event.key === 'Enter') {
                performSearch();
            }
        });
 


function openModal(hallId) {
    document.getElementById(`modal-${hallId}`).style.display = 'block';
}
function closeModal(hallId) {
    document.getElementById(`modal-${hallId}`).style.display = 'none';
}
