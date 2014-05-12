# sale_GOGgles

Watches [GOG.com](http://www.gog.com)'s ~~Fall~~ Spring Insomnia sale for you.

**Warning: quick 30 minute hack!**

## Install:
`pip install -r requirements.txt`
(or install [lxml](http://lxml.de) and [requests](http://www.python-requests.org) however you like...)

## Usage:

`sale_GOGgles.py`
With no args, prints current game on offer every 30 seconds.

If games are specified in arguments, it looks for a match, e.g. 
`sale_GOGgles.py System_Shock_2 Tomb_Raider_1+2+3`
looks for System Shock 2 and the Tomb Raider 1+2+3 pack.

Games must match exactly; I think the actual title should be the one from the
title of the page for the game itself, and replace spaces with underscores
e.g. for [Rollercoaster Tycoon 3](http://www.gog.com/game/rollercoaster_tycoon_3)
you'd use `sale_GOGgles.py Rollercoaster_Tycoon_3_Platinum!`

It just prints out "Game wanted!" if the on-sale game matches those you've
specified.

However, commented out is code for it to open a browser
window pointing to gog.com if a game matches. Uncomment the Linux or Windows
lines as appropriate. (I've tested the Linux xdg-open command on Ubuntu; not tested the Windows 
version.)

**The whole script's only been tested on Ubuntu, so your mileage may vary on Windows.**
