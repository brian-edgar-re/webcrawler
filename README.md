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

- **Error Handling**: Scrapy has built-in support for handling different types of HTTP errors and network-related issues. It automatically retries requests that fail due to transient network issues or server errors (5xx). You can customize the retry middleware (`RetryMiddleware`) to adjust the number of retries, retry codes, and backoff strategy. For client errors (4xx), Scrapy logs them, and you can handle them explicitly in your spider by checking the response status in your callback methods.

- **Concurrency and Scalability**: Scrapy is built on Twisted, an asynchronous networking framework, allowing it to handle a large number of requests concurrently. You can adjust settings like `CONCURRENT_REQUESTS`, `CONCURRENT_REQUESTS_PER_DOMAIN`, and `CONCURRENT_REQUESTS_PER_IP` to control concurrency levels. Scrapy is inherently asynchronous and does not use multi-threading or multi-processing for making HTTP requests but can be scaled horizontally (across multiple machines) for distributed crawling.

- **URL Tracking and Deduplication**: Scrapy automatically filters duplicate requests to the same URL using its `DUPEFILTER_CLASS`. This default deduplication mechanism ensures that Scrapy does not crawl the same URL more than once during a crawl. You can customize or disable this behavior as needed.

- **Storage and Data Management**: Scrapy provides several ways to store scraped data, including exporting to JSON, CSV, and XML files via feed exports. For more complex storage needs, you can write custom item pipelines to save data to databases or other storage systems. Scrapy's item pipelines provide a structured way to process and save data efficiently.

- **Distributed Crawling**: While Scrapy itself does not provide built-in support for distributed crawling, projects like Scrapy Cluster or Frontera can be used to distribute Scrapy spiders across multiple machines. These tools allow you to manage distributed crawls and aggregate data collected by multiple spiders.

- **Handling Redirects**: Scrapy handles redirects automatically by default, following HTTP 3xx responses according to the HTTP standard. The `RedirectMiddleware` can be configured to customize this behavior, such as limiting the number of redirects to follow or handling specific redirect scenarios. Scrapy also provides the `dont_redirect` request meta key to prevent redirect following for individual requests.

- **Legal and Ethical Guidelines**: Always adhere to legal and ethical guidelines when crawling websites. Obtain permission if required, and do not scrape personal or sensitive information without consent.


## Additional Tips

- **Debugging**: Use Scrapy's logging options to troubleshoot and debug your spider. Adjust the log level as needed to get more detailed output.
- **Customization**: Consider customizing the spider to fit your specific needs. This may include refining the selectors for extracting data, handling pagination, or adding functionality to process and analyze the data.