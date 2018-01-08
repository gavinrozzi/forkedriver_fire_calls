# This is a Python scraper that saves Forked River Fire Department calls for service. Copyright (C) 2017 Gavin Rozzi

# # Import dependencies
from lxml import html
import requests
import scraperwiki

# # Read in the FRFD call page
page = requests.get('http://www.forkedriverfire.com/firecallsstats.htm')
tree = html.fromstring(page.content)

## Select calls from page by XPath

# # Write out to the sqlite database using scraperwiki library
scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})