# Author: Brett Gaglione (brettgaglione.com)
# Date: April 11, 2017

import errno
import os

import mechanize
from time import sleep
from os.path import join

# why two browsers? ...google stackoverflow question
br1 = mechanize.Browser()
br2 = mechanize.Browser()

br1.open('https://downloads.khinsider.com/game-soundtracks/album/animal-crossing-gc-rip-')
f = open("source.html","w")
f.write(br1.response().read()) #can be helpful for debugging maybe

count = 0
path = "/Users/brettgaglione/PycharmProjects/game_soundtrack_downloader/downloads"

# makes sure path exists, if not, it creates it
try:
    os.makedirs(path)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise

for homepageLink in br1.links():
    if ".mp3" in str(homepageLink):

        if str(homepageLink.text) != "Download":
            br2.open(homepageLink.url)

            for actualLinkOfFile in br2.links(): #scans links in page
                if str(actualLinkOfFile.text) == "Click here to download": #if this is the link, download it
                    count += 1
                    br2.retrieve(str(actualLinkOfFile.url), join(path,  "track_"+ str(count) + ".mp3"))
                    print str(actualLinkOfFile) + " has been downloaded"
                    sleep(1) # so i dont hammer the website

