import os
import re
import shutil
import subprocess
from time import gmtime, strftime

import scrapy
from scrapy.selector import Selector

DEBUG = 0

def debug(msg):
    if DEBUG:
        print msg

DIRECTORY = 'html'
try:
    if os.path.exists(DIRECTORY):
        shutil.rmtree(DIRECTORY)
    os.makedirs(DIRECTORY)
    datetime = subprocess.check_output('date')
    with open('last_update', 'w') as f:
        f.write(datetime)
except Exception as e:
    print(e)

class LeetcodeTagSpider(scrapy.Spider):
    name = "leetcodeTag"
    allowed_domains = ["leetcode.com"]
    domain = "leetcode.com"
    start_urls = [
        "https://leetcode.com/problemset/algorithms/",
    ]

    def parse(self, response):
        tag_hrefs = response.selector.xpath('//a[contains(@href, "tag")]/@href').extract()
        tags = [href.split('/')[-2] for href in tag_hrefs]
        debug(tags)
        tag_urls = ["https://" + self.domain + href for href in tag_hrefs]
        debug(tag_urls)
        for url in tag_urls:
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        file = response.url.split("/")[-2] + '.html'
        path = os.path.join(DIRECTORY, file)
        with open(path, 'wb') as f:
            f.write(response.body)

        cmd = ["python", "parse.py", path]
        out, err = subprocess.Popen(
                       cmd,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE
                   ).communicate()
        print out.strip()
        if err:
            raise Exception(err)
