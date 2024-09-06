# Flask Web Scraping API

This is a Python server that provides an endpoint to scrape content from websites.

## Usage

- **`/scrap?url=<website>`**: Scrapes the content of the given URL and extracts text from `h1`, `h2`, `h3`, `h4`, `p`, and `div` tags.

### Example:

```
/scrap?url=https://example.com
```

### Scraping Result of Cloudilic [Link](https://flask-pi.vercel.app/scrap?url=https://cloudilic.com/)

![Scraping Result](https://imagizer.imageshack.com/img922/8347/TcryYq.png)

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:

   ```bash
   python api/index.py
   ```

3. Open `http://127.0.0.1:5000/` in your browser.

## Deployment

Deploy easily using Vercel:
