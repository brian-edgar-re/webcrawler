# Web Crawler Project

This document provides setup and usage instructions for the web crawler project. This crawler is designed to navigate web pages and extract URLs, with the results saved to a JSON file. It's built using Scrapy, a powerful web crawling and scraping framework for Python.

## Setup Instructions

### Prerequisites

- Python 3.9.6

### Creating a Virtual Environment

1. **Create a new virtual environment** named `env` by running the following command in your terminal:
   ```bash
   python3 -m venv env
   ```
2. **Activate the virtual environment**:
   - On Windows, run:
     ```bash
     env\Scripts\activate
     ```
   - On macOS and Linux, run:
     ```bash
     source env/bin/activate
     ```

### Installing Dependencies

Ensure you are in the project directory and your virtual environment is activated. Install the project dependencies by running:

```bash
pip3 install -r requirements.txt
```

## Web Crawler Details

The scraper is located at `webcrawler/crawler/crawler/spiders/example.py`. Before running the scraper, ensure you are in the correct directory where `scrapy.cfg` is located.

   ```bash
   cd crawler
   ```

### Running the Web Crawler

To start the web crawler, use the following command:

```bash
scrapy crawl example -o urls.json
```

- `scrapy crawl example`: This tells Scrapy to start crawling using the `example` spider.
- `-o urls.json`: This option outputs the crawled data to a file named `urls.json`. The file will contain the URLs extracted by the crawler in JSON format.

## Considerations

- **JavaScript-Rendered Websites**: This version of the web crawler does not handle websites that heavily rely on JavaScript for rendering content. To crawl such sites, consider integrating Selenium or similar tools that can execute JavaScript.

- **Rate Limiting and Politeness**: Be mindful of the load your crawler imposes on websites. Respect `robots.txt` and implement polite crawling practices, such as rate limiting and avoiding repeated crawls of the same page.

- **Legal and Ethical Guidelines**: Always adhere to legal and ethical guidelines when crawling websites. Obtain permission if required, and do not scrape personal or sensitive information without consent.

## Additional Tips

- **Debugging**: Use Scrapy's logging options to troubleshoot and debug your spider. Adjust the log level as needed to get more detailed output.
- **Customization**: Consider customizing the spider to fit your specific needs. This may include refining the selectors for extracting data, handling pagination, or adding functionality to process and analyze the data.

## Conclusion

This README provides a basic overview and setup instructions for running the web crawler. Adjust and expand upon this documentation as your project grows and evolves.
