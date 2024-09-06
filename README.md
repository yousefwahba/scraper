# Python Web Scraping API

This is a Flask server that provides an endpoint to scrape content from websites.

## Features

- Scrapes text content from the following HTML tags: `h1`, `h2`, `h3`, `h4`, `p`, and `div`.
- Simple GET request interface to extract text from any webpage.

## API Usage

### Endpoint

- **`/scrap?url=<website>`**: Scrapes the content of the provided URL.

### Example Request

To scrape the content of a website, make a request to the endpoint like this:

```bash
curl -X GET "https://scraper-py.vercel.app/scrap?url=https://example.com"
```

Or simply paste the URL into your browser:

```
https://scraper-py.vercel.app/scrap?url=https://example.com
```

### Response Format

The API returns a JSON object containing the extracted text from the target page. Example response:

```json
{
  "elements": {
    "h1": ["Heading 1 Text"],
    "h2": ["Subheading 1", "Subheading 2"],
    "h3": ["Another Subheading"],
    "h4": [],
    "p": ["Paragraph text content."],
    "div": ["Div content here."]
  },
  "url": "https://example.com/"
}
```

### Example:

Scraping the content of Cloudilic:

- **Request**:

  ```
  /scrap?url=https://cloudilic.com/
  ```

- **Response**:
  ![Scraping Result](https://imagizer.imageshack.com/img922/8347/TcryYq.png)

[Check it out here](https://flask-pi.vercel.app/scrap?url=https://cloudilic.com/)

---

## Setup

### Step 1: Install dependencies

Make sure you have Python installed, then install the necessary libraries:

```bash
pip install -r requirements.txt
```

### Step 2: Run the app

Run the Flask application with:

```bash
python api/index.py
```

### Step 3: Access the API

Open your browser and visit:

```
http://127.0.0.1:5000/
```

You can then use the `/scrap` endpoint to scrape websites.

---



## Deployment

This server is deployed on Vercel. You can access it [here](https://flask-pi.vercel.app/).

