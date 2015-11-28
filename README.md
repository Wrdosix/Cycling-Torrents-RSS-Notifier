# Cycling-Torrents-RSS-Notifier

I was tired of missing the early uploads for Grand Tour stages, so I decided to create a simple little Python script to query an RSS feed hosted by Cyclingtorrents.nl and display OSX push notifications with the name of the video, its size and a link to the download. At the website, one can customize the feed to show, say, only Cyclocross races. By giving the unique feed url as a command line argument to the script, the user is able customize the type of content he or she desires.

The script queries the feed once every 30 seconds using elements of the feedparser library (https://pypi.python.org/pypi/feedparser). In addition, this script utilizes the fantastic terminal-notifier command line tool (https://github.com/julienXX/terminal-notifier) to offer the user simple push notifications in OSX.
