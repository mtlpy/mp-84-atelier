#! /usr/bin/env python3

""" Generate a list of a Slack channel members based on a saved web page of 
that channel. 
"""

import sys
import bs4
from pprint import pprint

def main():
    data = open(sys.argv[1], "r")
    soup = bs4.BeautifulSoup(data, "lxml")
    spans = soup.select('span.c-member__primary_content')
    for el in spans:
        name = el.select_one("span.c-member_name").text
        name = name.replace("(you)", "")
        for emo in el.select("span.c-emoji"):
            img = emo.select_one("img")
            if img["alt"] == ":snake:":
                name += "🐍"
        print(name)

if __name__ == "__main__":
    main()
    
