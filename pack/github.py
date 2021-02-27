#!/usr/bin/env python
desc="""To-Do

CHANGELOG:
0.1.0
- 
"""
epilog="""Author:
manu.molinam@gmail.com

Barcelona, 26/02/2021
"""
import requests
from lxml import etree
from io import StringIO
from html.parser import HTMLParser

from .crawler import Crawler

class GitHub(Crawler):
    """
    This class represents the crawler search parameters.
    To be more flexible I've decided to separate the search 
    from the page on which the search is made
    ...

    Attributes
    ----------

    """
    def __init__(self, keywords, proxies, search_type, page=1):
        Crawler.__init__(self, keywords, proxies, search_type, page)
        self.url = "https://github.com{}"
        self.template = "https://github.com/search?q={}&type={}"

    def get_url_by_type(self):
        return self.template.format(self.keywords, self.search_type)

    
    def parser_get_links(self, tree):
        # This will get the anchor tags <a href...>
        refs = tree.xpath('//div[@class="f4 text-normal"]/a')
        # Get the url from the ref
        links = [link.get('href', '') for link in refs]
        # Return a list that only ends with .com.br
        return [{'url': self.url.format(l) if l.startswith('/') else l}  for l in links]

    def parser_get_content(self, url, proxy, use_proxy=True):    
        request_timeout = 10
        try:
            if use_proxy:
                page = requests.get(url, proxies=proxy, timeout=request_timeout)
            else:
                page = requests.get(url)
            
            parser = etree.HTMLParser()
            # Decode the page content from bytes to string
            html = page.content.decode("utf-8")
            tree = etree.parse(StringIO(html), parser=parser)
        except Exception as e:
            return False, 'There was a problem crawling the URL: "{}"'.format(e)
        
        return True, tree