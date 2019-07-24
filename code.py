import argparse
import webbrowser
import os
import sys
import requests
import json
from bs4 import BeautifulSoup

def open_link(url):
    webbrowser.open_new_tab(url)


def writeToJSONFile(path, fileName, data):
    filePathNameWithExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWithExt, 'w') as fp:
        json.dump(data, fp)


def fetch_metadata(url):
    path = ''
    fileName = 'details'
    jsonData = {}
    jsonData['map'] = []
    jsonData['map'].append({'url' : url})
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")

    metas = soup.find_all('meta')

    for meta in metas:
        if 'name' in meta.attrs and meta.attrs['name'] == 'description':
            jsonData['map'].append({'meta_description' : meta.attrs['content']})
        if 'name' in meta.attrs and meta.attrs['name'] == 'author':
            jsonData['map'].append({'author' : meta.attrs['content']})
        else :
            jsonData['map'].append({'author' : "null"})

    writeToJSONFile(path, fileName, jsonData)

def main(*args):
    if len(args) == 0:
        parser = argparse.ArgumentParser()
        parser.add_argument("--open", help="Open the url in a browser")
        args = parser.parse_args()
        openTerm = args.open
    else:
        openTerm = args[0]

    if not openTerm:
        print("Enter a valid url")
        sys.exit()

    open_link(openTerm)
    fetch_metadata(openTerm)

if __name__ == "__main__":
    main()
