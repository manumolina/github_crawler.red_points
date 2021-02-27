# Github crawler (Red Points)
> This script allows you to start the process of search a list of keywords 
in the GitHub webpage, crawl the results and save the links in a file.

Only one mandatory parameter are needed:
* input_path: the path to the json file with the data the user wants to search in the website.
The second parameter is the output path:
* output_path: the path to the folder where to save the results.
The results are saved in a file with the date of processing.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Contact](#contact)

## General info
This is a technical task composed of two coding exercises.
The first one consists of code a GitHub crawler that implements the GitHub search 
and returns all the links from the search result.

The second one is an extension of the previus task.
It consists of to extend it to extract also for each repository the owner of the repository
and the language stats.

## Technologies
* Python - version 3.6.3

## Setup
There is not needed to install special libraries or set up an environment.
All libraries used in this crawler are in the standard Python language.

## Code Examples
Search for a list of keywords and show the results to the screen:
`python main_json.py -i ./sample/input_1.json`
Search for a list of keywords and save the results in a file:
`python main_json.py -i ./sample/input_1.json -o ./output/`

## Features
This is the list of tasks requested and their status:
* Search for a list of keywords in the Github website
* Save the result in a file

To-do list:
* Search for a different page than the first one.

## Status
Project is: _in progress_

## Contact
Created by [@manumolina](https://github.com/manumolina) - I hope to hear from you soon.

