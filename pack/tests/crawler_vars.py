"""
name: crawler_vars.py
date: 2021-02-27
desc: constains battery of vars to test the Crawler class
"""
## ---------------------------
## test_template
## ---------------------------
test_template = {
    'input': {
        "keywords": [],
        "proxies": [],
        "type": ""
    },
    'output': None
}

## ---------------------------
## test_check_keywords_format
## ---------------------------
test_check_keywords_format = []
test_check_keywords_format_1 = {
    'input': { "keywords": [] },
    'output': ""
}
test_check_keywords_format_2 = {
    'input': { "keywords": None },
    'output': ""
}
test_check_keywords_format_3 = {
    'input': { "keywords": "" },
    'output': ""
}
test_check_keywords_format_4 = {
    'input': { "keywords": [ "openstack" ] },
    'output': "openstack"
}
test_check_keywords_format_5 = {
    'input': { "keywords": [ "openstack", "nova", "css" ] },
    'output': "openstack+nova+css"
}
test_check_keywords_format.append(test_check_keywords_format_1)
test_check_keywords_format.append(test_check_keywords_format_2)
test_check_keywords_format.append(test_check_keywords_format_3)
test_check_keywords_format.append(test_check_keywords_format_4)

## ---------------------------
## test_check_proxies
## ---------------------------
test_check_proxies = []
test_check_proxies_1 = {
    'input': { "proxies": [] },
    'output': 0
}
test_check_proxies_2 = {
    'input': { "proxies": None },
    'output': 0
}
test_check_proxies_3 = {
    'input': { "proxies": "" },
    'output': 0
}
test_check_proxies_4 = {
    'input': { "proxies": [ "194.126.37.94:8080", "13.78.125.167:8080" ] },
    'output': 2
}
test_check_proxies_5 = {
    'input': { "proxies": [ "194.126.37.94:8080", "13.78.125.167:8080", "13.78.125.167" ] },
    'output': 2
}
test_check_proxies.append(test_check_proxies_1)
test_check_proxies.append(test_check_proxies_2)
test_check_proxies.append(test_check_proxies_3)
test_check_proxies.append(test_check_proxies_4)
test_check_proxies.append(test_check_proxies_5)

## ---------------------------
## test_check_proxy_ip_address
## ---------------------------
test_check_proxy_ip_address = []
test_check_proxy_ip_address_1 = {
    'input': { "proxies": [] },
    'output': 0
}
test_check_proxy_ip_address_2 = {
    'input': { "proxies": None },
    'output': 0
}
test_check_proxy_ip_address_3 = {
    'input': { "proxies": "" },
    'output': 0
}
test_check_proxy_ip_address_4 = {
    'input': { "proxies": [ "194.126.37.94:8080", "13.78.125.167:8080" ] },
    'output': 2
}
test_check_proxy_ip_address_5 = {
    'input': { "proxies": [ "194.126.37.94:8080", "13.78.125.167:8080", "13.78.125.167" ] },
    'output': 3
}
test_check_proxy_ip_address.append(test_check_proxy_ip_address_1)
test_check_proxy_ip_address.append(test_check_proxy_ip_address_2)
test_check_proxy_ip_address.append(test_check_proxy_ip_address_3)
test_check_proxy_ip_address.append(test_check_proxy_ip_address_4)
test_check_proxy_ip_address.append(test_check_proxy_ip_address_5)

## ---------------------------
## test_check_proxy_port_address
## ---------------------------
test_check_proxy_port_address = test_check_proxies.copy()

## ---------------------------
## test_check_search_type
## ---------------------------
test_check_search_type = []
test_check_search_type_1 = {
    'input': { "search_type": None },
    'output': ""
}
test_check_search_type_2 = {
    'input': { "search_type": "" },
    'output': ""
}
test_check_search_type_3 = {
    'input': { "search_type": [] },
    'output': ""
}
test_check_search_type_4 = {
    'input': { "search_type": "Wikis" },
    'output': "wikis"
}
test_check_search_type_5 = {
    'input': { "search_type": "Wikipedia" },
    'output': ""
}
test_check_search_type.append(test_check_search_type_1)
test_check_search_type.append(test_check_search_type_2)
test_check_search_type.append(test_check_search_type_3)
test_check_search_type.append(test_check_search_type_4)
test_check_search_type.append(test_check_search_type_5)

"""
list of vars to test
"""
vars2test = { "test_template": test_template, "test_check_keywords_format": test_check_keywords_format,  
    "test_check_proxies": test_check_proxies, "test_check_proxy_ip_address": test_check_proxy_ip_address,
    "test_check_proxy_port_address": test_check_proxy_port_address, "test_check_search_type": test_check_search_type
}