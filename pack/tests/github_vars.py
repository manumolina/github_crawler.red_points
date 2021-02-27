"""
name: github_vars.py
date: 2021-02-27
desc: constains battery of vars to test the GitHub class
"""
## ---------------------------
## test_template
## ---------------------------
test_github_inputs = [
    { "keywords": [], "proxies": [], "type": "" },
    { "keywords": [ "openstack", "nova", "css" ], "proxies": [], "type": "" },
    { "keywords": [ "openstack", "nova", "css" ], "proxies": [ "194.126.37.94:8080" ], "type": "https://github.com/search?q=&type=" },
    { "keywords": [ "openstack", "nova", "css" ], "proxies": [ "194.126.37.94:8080", "13.78.125.167:8080", "13.78.125.167" ], "type": "Issues" }
]

## ---------------------------
## test_get_url_by_type
## ---------------------------
test_get_url_by_type = []
test_get_url_by_type_1 = { 'output': "" }
test_get_url_by_type_2 = { 'output': "https://github.com/search?q=openstack&nova&css&type=" }
test_get_url_by_type_3 = { 'output': "https://github.com/search?q=openstack&nova&css&type=" }
test_get_url_by_type_4 = { 'output': "https://github.com/search?q=openstack&nova&css&type=issues" }
test_get_url_by_type.append(test_get_url_by_type_1)
test_get_url_by_type.append(test_get_url_by_type_2)
test_get_url_by_type.append(test_get_url_by_type_3)
test_get_url_by_type.append(test_get_url_by_type_4)

## ---------------------------
## test_parser_get_links
## ---------------------------
test_parser_get_links = []
test_parser_get_links_1 = { 'output': 0 }
test_parser_get_links_2 = { 'output': 1 }
test_parser_get_links_3 = { 'output': 1 }
test_parser_get_links_4 = { 'output': 1 }
test_parser_get_links.append(test_parser_get_links_1)
test_parser_get_links.append(test_parser_get_links_2)
test_parser_get_links.append(test_parser_get_links_3)
test_parser_get_links.append(test_parser_get_links_4)

## ---------------------------
## parser_get_content
## ---------------------------
test_parser_get_content = []
test_parser_get_content = []
test_parser_get_content_1 = { 'output': [False, ''] }
test_parser_get_content_2 = { 'output': [True, ''] }
test_parser_get_content_3 = { 'output': [True, ''] }
test_parser_get_content_4 = { 'output': [True, ''] }
test_parser_get_content.append(test_parser_get_content_1)
test_parser_get_content.append(test_parser_get_content_2)
test_parser_get_content.append(test_parser_get_content_3)
test_parser_get_content.append(test_parser_get_content_4)

"""
list of vars to test
"""
vars2test = { "test_github_inputs": test_github_inputs,
    "test_get_url_by_type": test_get_url_by_type, "test_parser_get_links": test_parser_get_links, 
    "test_parser_get_content": test_parser_get_content
}