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
import re, random

class Crawler():
    """
    This class represents the crawler search parameters.
    To be more flexible I've decided to separate the search 
    from the page on which the search is made
    ...

    Attributes
    ----------
    keywords : str
        list of keywords to be searched as a query string 
    proxies : list
        list of proxies to be used during the request
    search_type : str
        type of object to filter the results
    page : int
        page number of the result to be saved (default 1)

    Methods
    -------
    check_keywords_format(keywords)
        ensures that all words have a correct format to be used later
    check_proxies(proxies)
        ensures that all proxies have a correct format to be used later. 
        we check ip structure and port. only the totally correct proxies can be used
    check_proxy_ip_address(proxies)
        ensures that all proxies have a correct ip format
    check_proxy_port_address(proxies)
        ensures that all proxies have a correct port format
    check_search_type(search_type)
        ensures the type of search is in the valid types
    get_random_proxy
        get a random proxy from the list and returns a dict 
        with the type of protocols to use
    """
    def __init__(self, keywords, proxies, search_type, page=1):
        self.keywords = self.check_keywords_format(keywords)
        self.proxies = self.check_proxies(proxies)
        self.search_type = self.check_search_type(search_type)
        self.page = page        
    
    def check_keywords_format(self, keywords: list)->str:
        """[summary] this function ensures that all words have 
        a correct format to be used later

        Args:
            keywords (str): list of keywords to be searched 

        Returns:
            [str]: list of keywords to be searched as a query string 
        """
        if not keywords:
            return ""
        clean_keywords = [keyword.strip() for keyword in keywords]        
        return "&".join(clean_keywords)

    def check_proxies(self, proxies: list)->list:
        """[summary] this function ensures that all proxies have 
        a correct format to be used later. we check ip structure and port.
        only the totally correct proxies can be used

        Args:
            proxies (list): list of proxies to be searched 

        Returns:
            list: list of proxies to be searched checked
        """
        if not proxies:
            return []
        clean_proxies = self.check_proxy_ip_address(proxies)
        clean_proxies = self.check_proxy_port_address(clean_proxies)
        return clean_proxies
    
    def check_proxy_ip_address(self, proxies: list)->list:
        """[summary] this function ensures that all proxies have 
        a correct ip format

        Args:
            proxies (list): list of proxies to be searched

        Returns:
            list: list of proxies to be searched with a correct ip
        """
        if not proxies:
            return []
        regex = "^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
        return [proxy for proxy in proxies if re.search(regex, proxy)]

    def check_proxy_port_address(self, proxies: list)->list:
        """[summary] this function ensures that all proxies have 
        a correct port format

        Args:
            proxies (list): list of proxies to be searched

        Returns:
            list: list of proxies to be searched with a correct port
        """
        if not proxies:
            return []
        return [proxy for proxy in proxies if re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', proxy)]

    def check_search_type(self, search_type: str)->str:
        """[summary] this function ensures the type of search is
        in the valid types

        Args:
            search_type (str): type of search selected

        Returns:
            str: the same search_type if is correct or empty string if not
        """
        if not search_type:
            return ""
        valid_types = ['repositories', 'issues', 'wikis']
        return search_type.lower() if search_type.lower() in valid_types else ""

    def get_random_proxy(self):
        """[summary] this function get a random proxy from the list
        and returns a dict with the type of protocols to use

        Returns:
            [dict]: list of proxies to use in every protocol
        """
        if not self.proxies:
            return {}
        
        proxy = self.proxies[random.randint(0, len(self.proxies)-1)]
        proxy_dict = { 
              "https" : proxy,
              "http": proxy
        }
        return proxy_dict
    
