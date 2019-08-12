import argparse
import webbrowser
import os
import sys
import requests
import json
from bs4 import BeautifulSoup
import re

def open_link(url):
    webbrowser.open_new_tab(url)

def writeToJSONFile(path, fileName, data):
    filePathNameWithExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWithExt, 'a+') as fp:
        json.dump(data, fp)

def read_sitemap():

    path = ''
    fileName = 'details'
    jsonData = {}
    jsonData['map'] = []

    f = open("sitemap.xml").read();
    locations = re.findall('<loc>(.*)</loc>', f)
    for loc in locations:
        tempUrl, titles, tempDesc, tempAuthor = fetch_metadata(loc)
        jsonData['map'].append({
            'url' : tempUrl,
            'title' : titles,
            'meta_description' : tempDesc,
            'author' : tempAuthor
        })
    writeToJSONFile(path, fileName, jsonData)

def fetch_metadata(url):
    
    tempUrl = url
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")

    metas = soup.find_all('meta')
    titles = soup.title.string

    for meta in metas:
        if 'name' in meta.attrs and meta.attrs['name'] == 'description':
            tempDesc = meta.attrs['content']
            break
        else:
            tempDesc = "null"
    
    for meta in metas:
        if 'name' in meta.attrs and meta.attrs['name'] == 'author':
            tempAuthor = meta.attrs['content']
            break
        else:
            tempAuthor = "null"

    return tempUrl, titles, tempDesc, tempAuthor;

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
    read_sitemap()

if __name__ == "__main__":
    main()
