import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CnnSpider(CrawlSpider):
    name = 'cnn'
    allowed_domains = ['cnn.com']
    start_urls = ['http://www.cnn.com']

    filename = 'links_%(name)s' % ({'name': name})
    open(filename, 'wb').close()

    rules = (
        # # Extract links matching 'category.php' (but not matching 'subsection.php')
        # # and follow links from them (since no callback means follow=True by default).
        # Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        with open(self.filename, 'ab') as f:
            f.write('referer.url : ' + response.request.headers.get('Referer', None) + '\n');
            # f.write('title       : ' + response.xpath('//title/text()').extract() + '\n');
            f.write('response.url: ' + response.url + '\n');
            f.write('depth       : ' + str(response.meta["depth"]) + '\n');
            f.write('-'*50 + '\n');
