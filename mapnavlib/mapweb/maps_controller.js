
console.log("executing script");

function updateMap(gesture) {
    // Adjust once gesture controls work
    let sensitivity = 100;

    switch (gesture) {
        case 'pan_left':
            map.panBy([-sensitivity, 0]);
            break;
        case 'pan_right':
            map.panBy([sensitivity, 0]);
            break;
        case 'pan_up':
            map.panBy([0, -sensitivity]);
            break;
        case 'pan_down':
            map.panBy([0, sensitivity]);
            break;
        case 'zoom_in':
            map.zoomIn();
            break;
        case 'zoom_out':
            map.zoomOut();
            break;
        default:
        // No recognized gesture
        break;
    }
}

// This is where gesture data is given
function recognizeGesture() {
    fetch('./mapnavlib/gestures.json')
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