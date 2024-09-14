from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from sitespider.items import genspiderItem

class MasterSpider(Spider):

    def start_requests(self):
        if hasattr(self,'parse_start'): # First page requiring a specific parser
            fcallback = self.parse_start
        else:
            fcallback = self.parse
        return [ Request(self.spd['start_url'],
                     callback=fcallback,
                     meta={'itemfields': {}}) ]

    def parse(self, response):
        sel = Selector(response)
        lines = sel.xpath(self.spd['xlines'])
        # ...
        for line in lines:
            item = genspiderItem(response.meta['itemfields'])               
            # ...
            # Get request_url of detailed page and scrap basic item info
            # ... 
            yield  Request(request_url,
                   callback=self.parse_item,
                   meta={'item':item, 'itemfields':response.meta['itemfields']})

        for next_url in sel.xpath(self.spd['xnext_url']).extract():
            if hasattr(self,'next_url_parser'): # Need to process the next page URL before?
                yield self.next_url_parser(next_url, response)
            else:
                yield Request(
                    request_url,
                    callback=self.parse,
                    meta=response.meta)

    def parse_item(self, response):
        sel = Selector(response)
        item = response.meta['item']
        for itemname, xitemname in self.spd['x_ondetailpage'].iteritems():
            item[itemname] = "\n".join(sel.xpath(xitemname).extract())
        return item


