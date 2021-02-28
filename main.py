#!/usr/bin/env python
desc="""This script allows the user to start the process of crawling the GitHub webpage
after searching for a list of keywords in a json file.

In this json file there are also a list of proxies to use during the request part
and a string with the type of search to filter the results.

The final motivation is to return a list of values with the results of the first page
Only one mandatory parameter is needed:
* input_path: the path to the json file with the data the user wants to search in the website.
To save the result in a json file you should add:
* output_path: the path to the folder where to save the results.

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

## --------------------------------------- ##
## JSON functions
## --------------------------------------- ##
def read_json_file(json_file_path: str)->dict:
    """[summary] this function read the json file 
    and return the values to use them in the crawler

    Args:
        json_file_path (str): path to the json file that contains data to execute the crawler

    Returns:
        dict: data read from json file and returned in json format
    """
    if not json_file_path:
        return {}
    data = {}
    try:
        with open(json_file_path) as f:
            data = json.load(f)
    except Exception:
        logging.error('Error reading JSON file')

    return data

def check_json_data_content(json_data:dict)->tuple:
    """[summary] this function check the data in the JSON file 
    has a correct structure

    Args:
        json_data (dict): data from input json file

    Returns:
        [bool]: the result of checking data
        [str]: empty string if all is ok, a message with the error if not 

    """
    if not json_data:
        message = 'JSON file is empty or something happended to the content'
        return False, message
    
    if not check_json_data_structure(json_data):
        message = 'JSON file not contains mandatory fields'
        return False, message
    return True, ''

def check_json_data_structure(json_data:dict)->bool:
    """[summary] this function check if all the fields needed
    are in the dictionary 

    Args:
        json_data (dict): data from input json file

    Returns:
        bool: True if all fields exist, False if not
    """
    if not json_data:
        return False
    fields = ['keywords', 'proxies', 'type']
    return all(list(map(lambda x: x in json_data.keys(), fields)))


## --------------------------------------- ##
## Github crawler functions
## --------------------------------------- ##
def check_github_crawler_values(github_crawler):
    """[summary] this function check after create the GitHub object
    if all attributes in object have a correct structure. 

    Args:
        github_crawler ([obj]): GitHub Crawler object

    Returns:
        [bool]: the result of checking attributes in the object
        [str]: empty string if all is ok, a message with the error if not 
    """
    status = True
    message = ""
    if not github_crawler.keywords:
        message += 'There was a problem with the keywords format\n'
        status = False
    
    if len(github_crawler.proxies) == 0:
        message += 'There was a problem with the proxies format'
        status = False
    
    if not github_crawler.search_type:
        message += 'There was a problem with the type format'
        status = False

    return status, message

def save_result(output_path: str, result: dict, verbose=False)->tuple:
    """[summary] this function save the result in a file 
    or show it in the screen 

    Args:
        output_path (str): path to the folder where save the results
        result (dict): links collected after the process

    Returns:
        [bool]: the result of save links in a file or show them in the screen
        [str]: links in a json format if all is ok, a message with the error if not 
    """
    if output_path:
        if not os.path.exists(output_path):
            return False, 'Output folder does not exists'
        filename = "{}.json".format(datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p"))
        output_file = os.path.join(output_path, filename)
        try:            
            with open(output_file, 'w') as f:
                json.dump(result, f, indent=4)
            f.close()
            message = 'Results saved in the file: {}\n'.format(output_file)
            logging.info(message)
            sys.stdout.write("[INFO] {}\n".format(message))
        except Exception as e:
            return False, 'There was a problem saving the output: {}'.format(e)
    else:
        sys.stdout.write("[INFO] {}\n".format(json.dumps(result, indent=4)))
    
    return True, json.dumps(result)

def launch_crawler_process(github_crawler)->tuple:
    """[summary] this function join the different process needed
    to prepare the crawler and extract the data

    Args:
        github_crawler ([obj]): GitHub Crawler object

    Returns:
        [bool]: the result of launch the crawler after all the steps
        [list]: links in a json format if all is ok, a message with the error if not 
    """
    selected_proxy = github_crawler.get_random_proxy()
    selected_url = github_crawler.get_url_by_type()
   
    status, content = github_crawler.parser_get_content(selected_url, selected_proxy, False)        
    if not status:
        return False, content

    links = github_crawler.parser_get_links(content)

    return True, links

def start_process(input_path: str, output_path: str, verbose=False)->tuple:
    """[summary] this functions start the process of the crawl.
    The steps are:
    * Read the JSON file
    * Check all the data have a correct format
    * Create the crawler object and check the 
    * Launch the process of extract information
    * Save the result

    Args:
        input_path (str): path to the input file
        output_path (str): path to the output file
        verbose (bool, optional): show more information on screen. Defaults to False.

    Returns:
        tuple: [description]
    """
    json_data = read_json_file(input_path)
    if verbose:
        sys.stdout.write("[INFO] {}\n".format(json_data))
    
    status, message = check_json_data_content(json_data)
    if not status:
        return False, message
    
    github_crawler = GitHub(json_data['keywords'], json_data['proxies'], json_data['type'])
    
    if verbose:    
        sys.stdout.write('------------------\n')
        sys.stdout.write('GitHub attributes\n')
        sys.stdout.write('------------------\n')
        sys.stdout.write("keywords: {}\n".format(github_crawler.keywords))
        sys.stdout.write("proxies: {}\n".format(github_crawler.proxies))
        sys.stdout.write("search_type: {}\n".format(github_crawler.search_type))
    
    status, message = check_github_crawler_values(github_crawler)
    if not status:
        ## check we have keywords, proxies and type
        return False, message

    status, result = launch_crawler_process(github_crawler)
    if not status:
        return False, result
    
    status, result = save_result(output_path, result, verbose)
    if not status:
        return False, result

    return True, result

def main():
    usage   = "%(prog)s [options] -v" 
    parser  = argparse.ArgumentParser(usage=usage, description=desc, epilog=epilog, \
                                      formatter_class=argparse.RawTextHelpFormatter)
  
    parser.add_argument("-v", "--verbose", default=False, action="store_true", 
        help="Display information during the process")
    parser.add_argument('--version', action='version', version=version, 
        help="Display version of this crawler")
    parser.add_argument("-i", "--input", dest="input_path", required=True,
        help="Path to the json file with the data the user wants to search in the website")
    parser.add_argument("-o", "--output", dest="output_path", default="",
        help="Path to the json file with the data the user wants to search in the website")
            
    o = parser.parse_args()
    if o.verbose:
        sys.stderr.write( "Options: %s\n" % str(o) )
    
    logging.info('------------------------')
    logging.info('Starting the crawler...')
    sys.stdout.write('[INFO] Starting the crawler...\n')

    if not os.path.exists(o.input_path):
        logging.error('JSON file not found')
        return
    status, result = start_process(o.input_path, o.output_path, o.verbose)
    if not status:
        logging.warning(result)
        sys.stdout.write("[ERROR] {}\n".format(result))
        return
    
    logging.info(result)
    logging.info('Crawler ended OK')
    logging.info('------------------------')
    sys.stdout.write('[INFO] Crawler ended OK\n')


if __name__=='__main__':
    t0 = datetime.now()
    try:
        main()
    except KeyboardInterrupt:
        sys.stderr.write("\nCtrl-C pressed!      \n")
    dt = datetime.now()-t0
    sys.stderr.write( "#Time elapsed: %s\n" % dt )


