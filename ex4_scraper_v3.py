"""
This is the final version.
See v1 and v2 how this is built from smaller pieces.

Still a very raw version as I didn't use the APIs and the custom library.
Instead I chose Selenium.

python3 ex4_scraper_v3.py

KMbappe 7.4M Followers
elonmusk 76.2M Followers
TheRealDonuldTrump None

TODO:
- make the logic for getting the 'Followers' information on Twitter Profile page
    more standardize and testable agaist future change (aka more resilient)
- make Selenium run in parallel so we save time when hitting more than one profile page.
- current output is text and should be convert to number
- only edge case support is where account doesn't exist the function returns None.
"""

import sys, os
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

HOME = os.path.abspath(os.getcwd())
sys.path.insert(0,HOME) # Set PATH. Add 'chromedriver' to path.


def get_twitter_followers(twitter_profile='KMbappe'):
    """Returns the profile count.
        This is unoptimized as we just use single Selenium driver in plain vanilla."""
    url = "https://twitter.com/%s" % twitter_profile
    # Optional argument, if not specified will search path.
    driver = webdriver.Chrome('./chromedriver')
    driver.get(url);
    try: # Start Scrapping!!
        time.sleep(5) # Let the user actually see something!
        # This is the page source.
        # src = driver.page_source
        # print(src) # For debug..

        # Find the target element containing the information we look for.

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

        follower_as_text = target_elm.text
        return follower_as_text
    except Exception as e:
        print("Scrape error.")
        print(e)
    finally:
        driver.quit()

if __name__ == '__main__':
    followers = get_twitter_followers()
    print('KMbappe', followers)
    followers = get_twitter_followers(twitter_profile='elonmusk')
    print('elonmusk', followers)
    followers = get_twitter_followers(twitter_profile='TheRealDonuldTrump')
    print('TheRealDonuldTrump', followers)
