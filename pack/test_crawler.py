import unittest

from crawler import Crawler
from tests.crawler_vars import vars2test

class CrawlerTest(unittest.TestCase):
    """[summary] this class tests 
    the methods of the Crawler object
    """
    
    template_test = vars2test['test_template']
    crawler_test = Crawler(template_test['input']['keywords'], 
                template_test['input']['proxies'], 
                template_test['input']['type'])

    def test_check_keywords_format(self):        
        for test in vars2test['test_check_keywords_format']:            
            result = self.crawler_test.check_keywords_format(test['input']['keywords'])
            self.assertTrue(result == test['output'])
        
    def test_check_proxies(self):
        for test in vars2test['test_check_proxies']:
            result = self.crawler_test.check_proxies(test['input']['proxies'])
            self.assertTrue(len(result) == test['output'])
        
    def test_check_proxy_ip_address(self):
        for test in vars2test['test_check_proxy_ip_address']:
            result = self.crawler_test.check_proxy_ip_address(test['input']['proxies'])
            self.assertTrue(len(result) == test['output'])
        
    def test_check_proxy_port_address(self):
        for test in vars2test['test_check_proxy_port_address']:
            result = self.crawler_test.check_proxy_port_address(test['input']['proxies'])
            self.assertTrue(len(result) == test['output'])
        
    def test_check_search_type(self):
        for test in vars2test['test_check_search_type']:
            result = self.crawler_test.check_search_type(test['input']['search_type'])
            self.assertTrue(result == test['output'])

    def test_get_random_proxy(self):
        self.assertTrue(True)
   

if __name__ == '__main__':
    unittest.main()