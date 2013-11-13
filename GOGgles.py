#!/usr/bin/env python
# encoding: utf-8
import time
import os
import sys

import requests
import lxml

GOG_URL = 'www.gog.com'


def get_front_page():
    r = requests.get(GOG_URL)
    return r.content


def get_sale_game_title(content):
    title_xpath = '//*[@id="giantSpotDisplay"]/div[1]/div/div/div/a[1]/text()'
    etree = lxml.html.fromstring(content)
    text = etree.xpath(title_xpath)
    return text


def main():
    try:
        games = sys.argv[1:]
    except IndexError:
        print 'Usage: sale_GOGgles.py Game_1 Game_2 Game_3'
        print 'e.g. sale_GOGgles.py System_Shock_2 FTL:_Faster_Than_Light'
        sys.exit()
    previous_title = None
#    while True:
    content = get_front_page()
    current_title = get_sale_game_title(content)
    print current_title
#        if get_sale_game_title(content) != previous_title:
#            check_title_wanted()
#        time.sleep(5)

if __name__ == '__main__':
    main()
