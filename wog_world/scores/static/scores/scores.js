// In your JavaScript file
function sendScore(score) {
    if (!(csrfToken && addPointsToScore && addScoreUrl)) {
        console.error('CSRF token is missing');
        return; // Exit if the CSRF token is not available
    }
    fetch(addScoreUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken  // Use the CSRF token variable
        },
        body: new URLSearchParams({
            'score': addPointsToScore
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

console.log("yeeyyyyy");