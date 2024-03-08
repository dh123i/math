document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var query = document.getElementById('queryInput').value;
    fetch('35.223.167.11.' + encodeURIComponent(query))
        .then(response => response.text())
        .then(data => {
            document.getElementById('searchResults').innerHTML = data;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
