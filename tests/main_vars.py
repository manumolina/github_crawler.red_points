"""
name: main_vars.py
date: 2021-02-27
desc: constains battery of vars to test the main script
"""
test_github_inputs = [
    { "keywords": [], "proxies": [], "type": "" },
    { "keywords": [ "openstack", "nova", "css" ], "proxies": [], "type": "" },
    { "keywords": [ "openstack", "nova", "css" ], "proxies": [ "194.126.37.94:8080" ], "type": "https://github.com/search?q=&type=" },
    { "keywords": [ "openstack", "nova", "css" ], "proxies": [ "194.126.37.94:8080", "13.78.125.167:8080", "13.78.125.167" ], "type": "Issues" }
]

## ---------------------------
## test_read_json_file
## ---------------------------
test_read_json_file = []
test_read_json_file_1 = {
    'input': { "json_file_path": None },
    'output': {}
}
test_read_json_file_2 = {
    'input': { "json_file_path": "" },
    'output': {}
}
test_read_json_file_3 = {
    'input': { "json_file_path": "./tests/test_input_1.json" },
    'output': {}
}
test_read_json_file_4 = {
    'input': { "json_file_path": "./tests/test_input_2.json" },
    'output': "{'keywords': ['openstack', 'nova', 'css'], 'proxies': ['194.126.37.94:8080', '13.78.125.167:8080']}"
}
test_read_json_file_5 = {
    'input': { "json_file_path": "./tests/test_input_3.json" },
    'output': "{'keywords': ['openstack', 'nova', 'css'], 'proxies': ['194.126.37.94:8080', '13.78.125.167:8080'], 'type': 'Issues'}"
}
test_read_json_file.append(test_read_json_file_1)
test_read_json_file.append(test_read_json_file_2)
test_read_json_file.append(test_read_json_file_3)
test_read_json_file.append(test_read_json_file_4)
test_read_json_file.append(test_read_json_file_5)

## ---------------------------
## test_check_json_data_content
## ---------------------------
test_check_json_data_content = []
test_check_json_data_content_1 = {
    'input': {
        'json_data': None
    },
    'output': False
}
test_check_json_data_content_2 = {
    'input': {
        'json_data': ""
    },
    'output': False
}
test_check_json_data_content_3 = {
    'input': {
        'json_data': { 'keywords': ['openstack', 'nova', 'css'], 'proxies': ['194.126.37.94:8080', '13.78.125.167:8080']}
    },
    'output': False
}
test_check_json_data_content_4 = {
    'input': {
        'json_data': { 'keywords': ['openstack', 'nova', 'css'], 'proxies': ['194.126.37.94:8080', '13.78.125.167:8080'], 'type': 'Issues'}
    },
    'output': True
}
test_check_json_data_content.append(test_check_json_data_content_1)
test_check_json_data_content.append(test_check_json_data_content_2)
test_check_json_data_content.append(test_check_json_data_content_3)
test_check_json_data_content.append(test_check_json_data_content_4)

## ---------------------------
## test_check_json_data_structure
## ---------------------------
test_check_json_data_structure = test_check_json_data_content.copy()

## ---------------------------
## test_check_github_crawler_values
## ---------------------------
test_check_github_crawler_values = test_check_json_data_content.copy()

## ---------------------------
## test_save_result
## ---------------------------
test_save_result = []
test_save_result_1 = {
    'input': {
        'path': None,
        'result': None
    },    
    'output': True
}
test_save_result_2 = {
    'input': {
        'path': '',
        'result': []
    },    
    'output': True
}
test_save_result_3 = {
    'input': {
        'path': '',
        'result': [ { "url": "https://github.com/TheusBoot/FastAPI/wiki/FastAPI%3F" } ]
    },    
    'output': True
}
test_save_result_4 = {
    'input': {
        'path': './folder-not-exists/',
        'result': [ { "url": "https://github.com/TheusBoot/FastAPI/wiki/FastAPI%3F" } ]
    },    
    'output': False
}
test_save_result_5 = {
    'input': {
        'path': './tests/output/',
        'result': [ { "url": "https://github.com/TheusBoot/FastAPI/wiki/FastAPI%3F" } ]
    },    
    'output': True
}
test_save_result.append(test_save_result_1)
test_save_result.append(test_save_result_2)
test_save_result.append(test_save_result_3)
test_save_result.append(test_save_result_4)
test_save_result.append(test_save_result_5)


"""
list of vars to test
"""
vars2test = { "test_github_inputs": test_github_inputs, 
    "test_read_json_file": test_read_json_file, 
    "test_check_json_data_content": test_check_json_data_content,
    "test_check_json_data_structure": test_check_json_data_structure,
    "test_check_github_crawler_values": test_check_github_crawler_values,
    "test_save_result": test_save_result

}