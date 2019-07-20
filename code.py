import argparse
import webbrowser
import os
import sys

def open_link(url):
    webbrowser.open_new_tab(url)

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

if __name__ == "__main__":
    main()
