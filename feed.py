import feedparser
from time import mktime
from datetime import datetime
from lxml import html
from slack import ReportNews
from db import check_entries, add_entries

def Feed(url=None):

    d = feedparser.parse(url)

    for i in d['entries']:
        dt      = datetime.fromtimestamp(mktime(i['published_parsed']))
        title   = i['title']
        link    = (i['link'])

        #summary
        try:
           f       = i['summary_detail']['value']
           tree    = html.fromstring(f)
           summary = tree.xpath('//p/text()')[0]
        except:
           summary = "No summary found"

        if check_entries(link):
            pass
        else:
            add_entries(title=title, link=link, timestamp=dt)
            ReportNews(title,link,summary)

import yaml
with open("conf.yml") as blogs:
   blog_lst = yaml.load(blogs)
   for b in blog_lst['blogs']:
       Feed(b)
