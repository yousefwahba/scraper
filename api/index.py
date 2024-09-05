from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Hello World endpoint
@app.route('/')
def hello_world():
    return '''
    <h1>Cloudilic Task</h1>
    <p>go to</p>
    <code>/scrap?url=https://example.com</code>
    <p>Replace <code>https://example.com</code> with the URL you want to scrape.</p>
    '''

# Scrap endpoint to get content of a webpage
@app.route('/scrap')
def scrap():
    # Get the URL from the query parameter
    url = request.args.get('url')

    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400

    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract h1, h2, h3, h4, p, and div tags
        elements = {}
        tags = ['h1', 'h2', 'h3', 'h4', 'p', 'div']
        for tag in tags:
            elements[tag] = [elem.get_text(strip=True) for elem in soup.find_all(tag)]

        # Return the extracted content as JSON
        return jsonify({
            'url': url,
            'elements': elements
        })

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
