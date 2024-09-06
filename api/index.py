from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def hello_world():
    return '''
    <h1>Cloudilic Task</h1>
    <p>go to</p>
    <code>/scrap?url=https://example.com</code>
    <p>Replace <code>https://example.com</code> with the URL you want to scrape.</p>
    '''

@app.route('/scrap')
def scrap():
    url = request.args.get('url')

    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        elements = {}
        tags = ['h1', 'h2', 'h3', 'h4', 'p', 'div']
        for tag in tags:
            elements[tag] = [elem.get_text(strip=True) for elem in soup.find_all(tag)]

        return jsonify({
            'url': url,
            'elements': elements
        })

    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
