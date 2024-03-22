
console.log("executing map_controller");

function updateMap(gesture) {
    // console.log("we cookin: ", gesture);

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
        console.log('no recognised gesture');
        break;
    }
}

// This is where gesture data is given
function recognizeGesture() {
    fetch('../gestures.json')
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
}, 750);