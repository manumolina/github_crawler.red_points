import unittest

from github import GitHub
from tests.github_vars import vars2test

class GithubTest(unittest.TestCase):
    """[summary] this class tests 
    the methods of the GitHub object
    """
   
    def test_get_url_by_type(self):
        for i, test in enumerate(vars2test['test_github_inputs']):
            github_test = GitHub(test['keywords'], 
                test['proxies'], 
                test['type'])            
            result = github_test.get_url_by_type()
            self.assertTrue(result == vars2test['test_get_url_by_type'][i]['output'])
         
    def test_parser_get_links(self):
        for i, test in enumerate(vars2test['test_github_inputs']):
            github_test = GitHub(test['keywords'], 
                test['proxies'], 
                test['type'])
            
            selected_proxy = github_test.get_random_proxy()
            selected_url = github_test.get_url_by_type()
            _, content = github_test.parser_get_content(selected_url, selected_proxy, False) 

            result = github_test.parser_get_links(content)
            self.assertTrue(len(result) >= vars2test['test_parser_get_links'][i]['output'])
    
    def test_parser_get_content(self):
        for i, test in enumerate(vars2test['test_github_inputs']):
            github_test = GitHub(test['keywords'], 
                test['proxies'], 
                test['type'])
            
            selected_proxy = github_test.get_random_proxy()
            selected_url = github_test.get_url_by_type()
            
            status, _ = github_test.parser_get_content(selected_url, selected_proxy, False)
            self.assertTrue(status == vars2test['test_parser_get_content'][i]['output'][0])

if __name__ == '__main__':
    unittest.main()