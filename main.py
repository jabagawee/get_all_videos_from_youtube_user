#! /usr/bin/env python

import sys
username = sys.argv[1]

import feedparser
import requests

url_base = "https://gdata.youtube.com/feeds/api/users/{}/uploads".format(username)
page = requests.get(url_base).text
start, stop = page.index("<openSearch:totalResults>"), page.index("</openSearch:totalResults>")
count = int(page[start + 25:stop])
url_base += "?&max-results=50&start-index={}"

video_urls = []

for index in range(1, count + 1, 50):
    url = url_base.format(index)
    feed = feedparser.parse(url)
    video_urls += [entry.link for entry in feed.entries]

for video_url in video_urls:
    print video_url
