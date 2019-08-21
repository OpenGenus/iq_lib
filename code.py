import argparse
import webbrowser
import os
import sys
import requests
import json
from bs4 import BeautifulSoup
import re
from trie import Trie

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
        parser.add_argument("--search", help="Search the article accordingly")
        args = parser.parse_args()
        searchTerm = args.search
    else:
        searchTerm = args[0]

    if not searchTerm:
        print("Enter a valid search Term")
        sys.exit()

    t = Trie()

    with open('data.json') as json_file:
        data = json.load(json_file)
        for key in data['map']:
            t.insert(key['value'].lower(),key['key'])

    if(t.search(searchTerm.lower())):
        open_link(t.search(searchTerm.lower()))
    else:
        print("No articles found related to {} keyword".format(searchTerm))

    read_sitemap()

if __name__ == "__main__":
    main()
