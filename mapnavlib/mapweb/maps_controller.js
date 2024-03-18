
console.log("executing script");

let map = L.map('map').setView([0, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

function updateMap(gesture) {
    // Adjust once gesture controls work
    let sensitivity = 100;

    switch (gesture) {
        case 'left':
            map.panBy([-sensitivity, 0]);
            break;
        case 'right':
            map.panBy([sensitivity, 0]);
            break;
        case 'up':
            map.panBy([0, -sensitivity]);
            break;
        case 'down':
            map.panBy([0, sensitivity]);
            break;
        case 'zin':
            map.zoomIn();
            break;
        case 'zout':
            map.zoomOut();
            break;
        default:
        // No recognized gesture
        break;
    }
}

// This is where gesture data is given
function recognizeGesture() {
    fetch('../../gestures.json')
        .then(response => response.json())
        .then(data => {
            let gesture = data.gesture;
            if (gesture) {
                updateMap(gesture);
            }
        })
        .catch(error => console.log('Error fetching gesture data:', error));
}

setInterval(function() {
    recognizeGesture();
}, 100); // Adjust once gesture controls work