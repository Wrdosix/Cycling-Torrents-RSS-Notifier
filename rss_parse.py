import feedparser
import os
import time
import sys

#uses cyclingtorrents' RSS feed to check for new torrents every 30 seconds

#class for RSS feeds
class Feed:
    def __init__(self, url):
        self.url = url

    def setTopEntry(self):
        entryList = feedparser.parse(self.url)
        self.curTop = entryList.entries[0]

    def setSize(self):
        string = self.curTop.description
        sizeIndex = string.find('Size:')
        sizeSub = string[sizeIndex:sizeIndex+15]
        endIndex = sizeSub.find('B')
        self.size = sizeSub[0:endIndex+1]

    def getTop(self):
        return self.curTop

    def getLink(self):
        return self.curTop.link

    def getTitle(self):
        return self.curTop.title

    def getDescription(self):
        return self.curTop.description

    def getSize(self):
        return self.size

# notifier function (using terminal-notifier)
def notify(title, subtitle, message, url):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    snd = '-sound default'
    l = '-open {!r}'.format(url)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s, snd, l])))



##___________________________Main Program Body______________________##

# initial notification

notify(title    = 'Welcome!',
       subtitle = '',
       message  = 'I\'ll be sure to let you know if there\'s a new torrent!',
       url = 'http://www.cyclingtorrents.nl')

#construct initial feed object

initFeed = Feed(sys.argv[1])
initFeed.setTopEntry()
initFeed.setSize()

print initFeed.getTitle()
print initFeed.getLink()
print initFeed.getSize()

#construct new feed object every 30 seconds and compare to initial

while (1):
    curFeed = Feed(sys.argv[1])
    curFeed.setTopEntry()
    curFeed.setSize()

    if (curFeed.getLink() != initFeed.getLink()):
        initFeed = curFeed
        notify(title    = 'New torrent available!',
        subtitle = str(curFeed.getTitle()),
        message  = str(curFeed.getSize()),
        url = str(curFeed.getLink()))

    del curFeed
    time.sleep(30)
