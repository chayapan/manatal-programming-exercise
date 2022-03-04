"""
Exercise 4: Scraping Test
Write a Python program to get the number of followers of a specific account on
Twitter (taking an URL as an input, for example, https://twitter.com/KMbappe)

Time: 2-3 hours.
- First got stuck trying to parse HTML on dynamic page.
- Then configure Selenium for Mac environment.
- Once these two pieces are ready, only spend 5-10 minutes on the final prototype.
- I had to slept over a night to think about whether to use Twitter API or use Selenium...


Required library:
python3 -m pip install lxml selenium

Use lxml. https://lxml.de/parsing.html#parsing-html
- direct parsing of the page didn't work. It seem they use dynamically

There are APIs and library such as
- https://github.com/twintproject/twint
but these seem too good to be true. You can just pay Twitter for the data feed.

Stackoverflow suggests Selenium...
https://stackoverflow.com/questions/68987825/problem-while-scraping-twitter-using-beautiful-soup
https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path

Downlod chromiumdriver from. Select appropriate Chrome version and host system's spec.
https://chromedriver.chromium.org/downloads
See usage instruction
https://chromedriver.chromium.org/getting-started

See ex4_scraper_selinium.py for the implementation.
"""

import requests
from lxml import etree
from lxml import html
from lxml.etree import tostring
from io import StringIO
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://twitter.com/KMbappe"

r = requests.get(url)
print(r.status_code) # 200
print(r.encoding) # utf-8
# print(r.content)

try:
    # parser = etree.HTMLParser()
    # tree   = etree.parse(r.content, parser)

    # Parse HTML
    tree   = html.fromstring(r.content)

    # all tags
    elm = tree.xpath('//a')
    for e in elm:
       print(e.text) # See if we can get the "XXX Followers" info from <a> tag.

    # Pretty HTML page
    result = etree.tostring(tree,
                        pretty_print=True, method="html")
    print(result)
except Exception as e:
    print(e)

try:
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()
except Exception as e:
    print(e)
