#!/usr/bin/env python
# encoding: utf-8
import datetime
import time
import sys
import subprocess

import requests
import lxml.html

GOG_URL = 'http://www.gog.com'


def get_front_page():
    """
    Returns content of gog.com front page.
    """
    r = requests.get(GOG_URL)
    return r.content


def get_sale_game_title(content):
    """
    Return the current on-sale game title
    """
    title_xpath = '//*[@id="giantSpotDisplay"]/div[1]/div/div/div/a[1]/text()'
    etree = lxml.html.fromstring(content)
    text = etree.xpath(title_xpath)[0].strip()
    return text


def check_title_wanted(current_title, games):
    """
    Return True if game is in list of games from args.
    Games in args should have underscores instead of spaces.
    """
    current_title_with_underscores = current_title.replace(' ', '_')
    for game in games:
        if current_title_with_underscores == game:
            return True


def main():
    """
    Warning: quick 30 minute hack.
    Usage: sale_GOGgles.py

    With no args, continually prints current game on offer otherwise
    looks for a match to games in args
    e.g. sale_GOGgles.py System_Shock_2 Tomb_Raider_1+2+3
    Games must match exactly; get the actual title from the game banner on the
    page, and replace spaces with underscores
    e.g. for http://www.gog.com/game/rollercoaster_tycoon_3
    you'd use sale_GOGgles.py Rollercoaster_Tycoon_3_Platinum!
    """
    try:
        games = sys.argv[1:]
    except IndexError:
        print "No games specified"
        print "Going to just print current game instead"
        games = None

    previous_title = None
    while True:
        content = get_front_page()
        current_title = get_sale_game_title(content)
        print datetime.datetime.now().time(), current_title
        if current_title != previous_title and \
                check_title_wanted(current_title, games):
            print "Game wanted!"
            # here, we could launch a browser pointing to GOG
            # uncomment
            # Ubuntu launch browser
            # subprocess.call(['xdg-open', GOG_URL])
            # For Windows, something like this might work (not tested):
            # subprocess.call['start', '"www.gog.com"']
        previous_title = current_title
        time.sleep(10)

if __name__ == '__main__':
    main()
