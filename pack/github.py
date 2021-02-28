#!/usr/bin/env python
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
    url : str
        url used as a template in case the link is a relative path 
    query_template: str
        query url used as a template to include keywords and search type

    Methods
    -------
    get_url_by_type()
        include the keywords and the search type to the github template url
    
    parser_get_links
        recives a lxml tree object with the content of the webpage and search
        and returns a list with the links found

    parser_get_content
        get the commplete webpage from the url selected, convert it to html 
        and parse into string
    """
    def __init__(self, keywords, proxies, search_type, page=1):
        Crawler.__init__(self, keywords, proxies, search_type, page)
        self.url_template = "https://github.com{}"
        self.query_template = "https://github.com/search?q={}&type={}"

    def get_url_by_type(self):
        """[summary] this function include the keywords and the search type
        to the github template url

        Returns:
            [str]: github url with keywords and the search type added
        """
        if not self.keywords:
            return ""
        
        return self.query_template.format(self.keywords, self.search_type)

    
    def parser_get_links(self, tree):
        """[summary] this function recives a lxml tree object 
        with the content of the webpage and search:
        * <div> tags with a specific class
        * <a> tags inside the previous divs
        Return a list with links found in that tag

        Args:
            tree ([lxml tree]): contains the html data converted to lxml tree

        Returns:
            [list]: a list with the links found in the html webpage
        """
        if not tree or type(tree) == str:
            return []
        # This will get the anchor tags <a href...>
        refs = tree.xpath('//div[@class="f4 text-normal"]/a')
        # Get the url from the ref
        links = [link.get('href', '') for link in refs]
        # Return a list that only ends with .com.br
        return [{'url': self.url_template.format(l) if l.startswith('/') else l}  for l in links]

    def parser_get_content(self, url, proxy, use_proxy=True):
        """[summary] this function get the commplete webpage from the url selected,
        convert it to html and parse into string

        Args:
            url ([str]): url selected to crawl
            proxy ([dict]): contains the proxies to use in the request
            use_proxy (bool, optional): add the posibility to use proxies or not. 
                Defaults to True.

        Returns:
            [bool]: the result of parse the webpage
            [lxml tree]: contains the html data converted to lxml tree
        """
        if not url:
            return False, 'There was a problem with the URL: "{}"'.format(url)
        
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