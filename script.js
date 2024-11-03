console.log("hello");

function clicked(){
    window.location.href = 'addEvent.html';
}

/*fetch('http://169.234.5.101:8000/').then(res=> res.json()).then(response => {
    console.log(response);
})*/

async function fetchEvents() {
    try {
        const response = await fetch('http://127.0.0.1:5000/'); // URL to your Flask backend
        const events = await response.json(); // Parse the JSON response

        const eventList = document.getElementById('eventList');

        events.forEach(event => {
            const eventDiv = document.createElement('div');
            eventDiv.className = 'event';
            eventDiv.innerHTML = `
                <h2>${event.name}</h2>
                <p>Location: ${event.location}</p>
                <p>Major: ${event.major}</p>
                <p>Class: ${event.class}</p>
                <p>Professor: ${event.professor}</p>
                <p>Date: ${event.date}</p>
                <p>Time: ${event.time}</p>
            `;
            eventList.appendChild(eventDiv);
        });
    } catch (error) {
        console.error('Error fetching events:', error);
    }
}

document.addEventListener('DOMContentLoaded', fetchEvents);
