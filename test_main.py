import unittest
from main import read_json_file, check_json_data_content, check_json_data_structure, \
    check_github_crawler_values, save_result
from tests.main_vars import vars2test
from pack.github import GitHub

class MainTest(unittest.TestCase):

    def test_read_json_file(self):
        """[summary] 
        Func: read_json_file
        Desc: read the json file and return the values to use them in the crawler
        """
        for test in vars2test['test_read_json_file']:
            result = read_json_file(test['input']['json_file_path'])
            self.assertTrue(str(result) == str(test['output']))

    def test_check_json_data_content(self):
        """[summary] 
        Func: check_json_data_content
        Desc: check the data in the JSON file has a correct structure
        """
        for test in vars2test['test_check_json_data_content']:
            status, _ = check_json_data_content(test['input']['json_data'])
            self.assertTrue(status == test['output'])
    
    def test_check_json_data_structure(self):
        """[summary] 
        Func: check_json_data_structure
        Desc: check if all the fields needed are in the dictionary 
        """
        for test in vars2test['test_check_json_data_structure']:
            result = check_json_data_structure(test['input']['json_data'])
            self.assertTrue(result == test['output'])
    
    def test_check_github_crawler_values(self):
        """[summary] 
        Func: check_github_crawler_values
        Desc: check after create the GitHub object if all attributes in object have a correct structure. 
        """
        for i, test in enumerate(vars2test['test_github_inputs']):
            github_test = GitHub(test['keywords'], 
                test['proxies'], 
                test['type'])            
            status, result = check_github_crawler_values(github_test)
            self.assertTrue(status == vars2test['test_check_github_crawler_values'][i]['output'])

    def test_save_result(self):
        """[summary] 
        Func: save_result
        Desc: save the result in a file or show it in the screen 
        """
        for test in vars2test['test_save_result']:
            status, _ = save_result(test['input']['path'], test['input']['result'])
            self.assertTrue(status == test['output'])

if __name__ == '__main__':
    unittest.main()