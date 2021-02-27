import unittest
from main import read_json_file, check_json_data_content, check_json_data_structure, check_github_crawler_values
from tests.main_vars import vars2test
from pack.github import GitHub

class MainTest(unittest.TestCase):

    def test_read_json_file(self):
        for test in vars2test['test_read_json_file']:
            print(test)
            result = read_json_file(test['input']['json_file_path'])
            print(result)
            print(test['output'])
            self.assertTrue(str(result) == str(test['output']))

    def test_check_json_data_content(self):
        for test in vars2test['test_check_json_data_content']:
            print(test)
            status, _ = check_json_data_content(test['input']['json_data'])
            self.assertTrue(status == test['output'])
    
    def test_check_json_data_structure(self):
        for test in vars2test['test_check_json_data_structure']:
            print(test)
            result = check_json_data_structure(test['input']['json_data'])
            print(result)
            self.assertTrue(result == test['output'])
    
    def test_check_github_crawler_values(self):
        for i, test in enumerate(vars2test['test_github_inputs']):
            github_test = GitHub(test['keywords'], 
                test['proxies'], 
                test['type'])            
            print(test)
            result = check_github_crawler_values(github_test)
            print(result)
            self.assertTrue(result == vars2test['test_get_url_by_type'][i]['output'])

    # def test_launch_crawler_process(self):
    #     pass
    
    # def test_save_result(self):
    #     pass
    
    
    
    
    
    
    
if __name__ == '__main__':
    unittest.main()