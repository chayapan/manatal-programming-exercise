#!/usr/bin/env python3
"""
- Check chrome version - chrome://version/
- Mine is at version 98.

 Message: 'chromedriver' executable needs to be in PATH
 - The chromedriver  binary co-exists in this same project folder.
 - For Mac, first time the OS will complain about unidentified developer.
 - Then go to 'Security & Privacy' to allow the 'chromedriver' bin to run.

See Locating Elements:
 - https://selenium-python.readthedocs.io/locating-elements.html

 - https://stackoverflow.com/questions/861008/xpath-partial-of-attribute-known
"""
import sys, os
import time

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

HOME = os.path.abspath(os.getcwd())
sys.path.insert(0,HOME) # Set PATH. Add 'chromedriver' to path.

url = "https://twitter.com/KMbappe"
# inspect of the page shows that the information is link tag with destination
# https://twitter.com/<twitter-handle>/followers"

# Optional argument, if not specified will search path.
driver = webdriver.Chrome('./chromedriver')
driver.get(url);

try: # Start Scrapping!!
    time.sleep(5) # Let the user actually see something!

    # For search box hitting.
    # search_box = driver.find_element_by_name('q')
    # search_box.send_keys('ChromeDriver')
    # search_box.submit()

    # Get links on page.
    # time.sleep(5) # Let the user actually see something!
    # links = driver.find_elements(by=By.TAG_NAME, value='a')
    # for l in links:
    #     print(l)

    # Find the target element.

    # Use Xpath.
    # In Chrome, just use $x("//a") in console to try several XPath expression.
    # Like this $x("//a[contains(@href,'followers')]")
    # And here is the XPath
    #
    #   //a[contains(@href,'followers')]
    #
    # Which returns a list
    # So,
    # $x("//a[contains(@href,'followers')]")[0].text
    # '7.4M Followers'

    # Translate to selenium
    target_elm = driver.find_element(By.XPATH, "//a[contains(@href,'followers')]")
    # Returns
    #   selenium.webdriver.remote.webelement.WebElement
    print("Followers count from browser.")
    print(target_elm)
    print(target_elm.text) # This returns '7.4M Followers'

    # This is the page source.
    # src = driver.page_source
    # print(src)
except Exception as e:
    print("Scrape error.")
    print(e)
finally:
    driver.quit()
