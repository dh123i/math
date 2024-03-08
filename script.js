document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var query = document.getElementById('queryInput').value;
    fetch('https://https://b1c8e562-5e2b-4ab2-9cbe-f52f341baf33-00-2audkqvrsq8jd.riker.replit.dev//search?query=' + encodeURIComponent(query))
        .then(response => response.text())
        .then(data => {
            document.getElementById('searchResults').innerHTML = data;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
