import argparse
import webbrowser
import os
import sys
import requests
from bs4 import BeautifulSoup

def open_link(url):
    webbrowser.open_new_tab(url)

def fetch_metadata(url):
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")

    metas = soup.find_all('meta')

    for meta in metas:
        if 'name' in meta.attrs and meta.attrs['name'] == 'description':
            print(meta.attrs['content'])
        if 'name' in meta.attrs and meta.attrs['name'] == 'author':
            print(meta.attrs['content'])

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
