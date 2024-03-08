document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var query = document.getElementById('queryInput').value;
    fetch('https://your-replit-app-name.repl.co/search?query=' + encodeURIComponent(query))
        .then(response => response.text())
        .then(data => {
            document.getElementById('searchResults').innerHTML = data;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
