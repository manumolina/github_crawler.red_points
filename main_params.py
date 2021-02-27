#!/usr/bin/env python
desc="""This script allows the user to start the process of crawler the GitHub webpage
after search for a list of keywords.
The final motivation is to return a list of values with the results of the first page
Three mandatory parameters are needed:
* keywords: the list of keywords the user wants to search in the website.
            no filter or limit included.
* proxies: the list of proxies the user wants to pass throug
            no filter or limit included.
* type: the type of object the user wants to search for
        limited to 3 values -> Repositories (repos), Issues (issues) and Wikis (wikis)

CHANGELOG:
0.1.0
- 
"""
epilog="""Author:
manu.molinam@gmail.com

Barcelona, 26/02/2021
"""
version="0.1.0"
import argparse, os, sys, time, json
import requests
import logging
logging.basicConfig(filename='output.log' , format='%(asctime)s | %(levelname)s: %(message)s', level=logging.DEBUG)
from datetime import datetime
from pack.github import GitHub

from lxml import etree
from io import StringIO
from html.parser import HTMLParser

def start_crawler(keywords: str, proxies: list, search_type: str, page: int):
    github_crawler = GitHub(keywords, proxies, search_type, page)
    links = get_links(tree)
    print(links)

# Call this function and pass in your tree
def get_links(tree):
    # This will get the anchor tags <a href...>
    refs = tree.xpath('//div[@class="f4 text-normal"]/a')
    # Get the url from the ref
    links = [link.get('href', '') for link in refs]
    # Return a list that only ends with .com.br
    return [l for l in links]


def main():
    usage   = "%(prog)s [options] -v" 
    parser  = argparse.ArgumentParser(usage=usage, description=desc, epilog=epilog, \
                                      formatter_class=argparse.RawTextHelpFormatter)
  
    parser.add_argument("-v", "--verbose", default=False, action="store_true", 
        help="Display information during the process")
    parser.add_argument('--version', action='version', version=version, 
        help="Display version of this crawler")
    parser.add_argument("-k", "--keywords", dest="keywords", required=True, 
        help="List of keywords to be searched separated by commas")
    parser.add_argument("-x", "--proxies", dest="proxies", required=True, 
        help="List of proxies to be used during the request separated by commas")
    parser.add_argument("-t", "--type", dest="search_type", required=True, 
        help="Type of object to filter the results")
    parser.add_argument("-p", "--page",  default=1, type=int, 
        help="Page number of the result to be saved  [%(default)s]")
        
    o = parser.parse_args()
    if o.verbose:
        sys.stderr.write( "Options: %s\n" % str(o) )
    
    start_crawler(o.keywords, o.proxies, o.search_type, o.page)

if __name__=='__main__':
    t0 = datetime.now()
    try:
        main()
    except KeyboardInterrupt:
        sys.stderr.write("\nCtrl-C pressed!      \n")
    dt = datetime.now()-t0
    sys.stderr.write( "#Time elapsed: %s\n" % dt )


