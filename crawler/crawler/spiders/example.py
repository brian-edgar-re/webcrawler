import scrapy
from bs4 import BeautifulSoup


class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ["https://example.com"]

    def parse(self, response):
        soup = BeautifulSoup(response.body.decode('utf-8'), 'html5lib')
        
        # Extract all links on the page and follow them
        links = soup.find_all('a')
        for link in links:
            url = link.get('href')
            text = link.string
            self.logger.info(f'Link URL: {url}, Link Text: {text}')

            if url is not None:
                # Before following, save the found URL
                yield {'url': response.urljoin(url)}  # Ensure the URL is absolute
                
                # Now follow the URL to parse detail page
                yield response.follow(url, callback=self.parse)
