document.getElementById('recForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const location = document.getElementById('recLocation').value;

    // Fetch recommendations from the backend
    fetch('/getRec', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ recLocation: location }), // Sending the location in the request body
    })
    .then(response => response.json()) // Parse JSON response
    .then(data => {
        const recContainer = document.querySelector('.recContainer');
        recContainer.innerHTML = ''; // Clear previous recommendations

        // Check if recommendations are returned
        if (data.length === 0) {
            recContainer.innerHTML = '<p>No recommendations found for this location.</p>';
            return;
        }

        // Create recommendation cards for each cafe
        data.forEach(cafe => {
            const card = document.createElement('div');
            card.className = 'recommendationCard';

            const nameElement = document.createElement('h2');
            nameElement.className = 'cafeName';
            nameElement.textContent = cafe.name;

            const locationElement = document.createElement('p');
            locationElement.className = 'cafeLocation';
            locationElement.textContent = `Location: ${cafe.address}`;

            const picsContainer = document.createElement('div');
            picsContainer.className = 'recPics';

            // Create images for the cafe
            cafe.image_url.forEach(photoUrl => {
                const img = document.createElement('img');
                img.src = photoUrl;
                img.alt = cafe.name;
                img.className = 'cafeImage';
                picsContainer.appendChild(img);
            });

            // Append all elements to the card
            card.appendChild(nameElement);
            card.appendChild(locationElement);
            card.appendChild(picsContainer);
            recContainer.appendChild(card); // Append card to recommendations container
        });
    })
    .catch(error => console.error('Error fetching recommendations:', error));
});
