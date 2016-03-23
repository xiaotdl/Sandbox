import os
import random

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request, HtmlResponse
from scrapy.utils.spider import iterate_spider_output


class RandomCrawlSpider(CrawlSpider):

    def __init__(self, *a, **kw):
        super(RandomCrawlSpider, self).__init__(*a, **kw)

    def _requests_to_follow(self, response):
        if not isinstance(response, HtmlResponse):
            return
        seen = set()
        for n, rule in enumerate(self._rules):
            links = [l for l in rule.link_extractor.extract_links(response) if l not in seen]
            if links and rule.process_links:
                links = rule.process_links(links)
            for link in links:
                seen.add(link)
                r = Request(url=link.url, callback=self._response_downloaded, dont_filter=True)
                r.meta.update(rule=n, link_text=link.text)
                yield rule.process_request(r)

    def _parse_response(self, response, callback, cb_kwargs, follow=True):
        if callback:
            cb_res = callback(response, **cb_kwargs) or ()
            cb_res = self.process_results(response, cb_res)
            for requests_or_item in iterate_spider_output(cb_res):
                yield requests_or_item

        if follow and self._follow_links:
            _req_to_follow = list(self._requests_to_follow(response))
            if _req_to_follow:
                _req_to_follow = [random.choice(_req_to_follow)]
            for request_or_item in _req_to_follow:
                yield request_or_item


class DepthSpider(RandomCrawlSpider):
    name = 'depth_spider'
    start_urls = None
    domain_name = None
    first_resp = True
    rules = (
        Rule(LinkExtractor(allow_domains=domain_name), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        if self.first_resp:
            print response.request.headers.get('Referer', None)
            self.first_resp = False
        print response.url

