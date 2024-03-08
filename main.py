import requests
from flask import Flask, request, Response, render_template_string

app = Flask(__name__)

# HTML template for the search form
search_form_html = '''
<!DOCTYPE html>
<html>
<head>
    <title>Google Search Proxy</title>
</head>
<body>
    <h1>Welcome to the Google Search Proxy!</h1>
    <form action="/search" method="GET">
        <input type="text" name="query" placeholder="Enter your search query">
        <button type="submit">Search</button>
    </form>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(search_form_html)

@app.route('/search')
def search():
    # Retrieve the 'query' parameter from the query string
    query = request.args.get('query')

    # Check if the 'query' parameter is provided
    if not query:
        return 'Missing query parameter', 400

    try:
        # Construct the Google search URL
        google_url = f"https://www.google.com/search?q={query}"

        # Fetch the content of the Google search results page
        response = requests.get(google_url)
        if response.status_code == 200:
            # Return the content of the Google search results page to the client
            return Response(response.content, content_type=response.headers['content-type'])
        else:
            # If the request to the Google search URL fails, return an error message
            return 'Failed to fetch Google search results: ' + str(response.status_code), response.status_code
    except Exception as e:
        # If an error occurs during the request, return an error message
        return 'Error fetching Google search results: ' + str(e), 500

if __name__ == '__main__':
    # Run the Flask application on host 0.0.0.0 and port 8080
    app.run(host='0.0.0.0', port=8080)
