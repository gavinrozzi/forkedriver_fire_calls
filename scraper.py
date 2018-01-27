## This is a Python scraper that saves Forked River Fire Department calls for service. Copyright (C) 2018 Gavin Rozzi

## Import dependencies
import lxml
from lxml import html
import requests
import scraperwiki

## Read in the FRFD call page
page = requests.get('http://www.forkedriverfire.com/firecallsstats.htm')
tree = html.fromstring(page.content)

## Select calls from page by XPath
firecalls = tree.xpath('//div//p/text()')

## Define Data
data = {
        'firecalls': 'firecalls'     
}

print data

## Write out to the sqlite database using scraperwiki library
scraperwiki.sqlite.save(data=data)
