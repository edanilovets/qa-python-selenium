#
# Firefox run setup
#
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
    driver = webdriver.Firefox(firefox_binary=binary)
    driver.get("http://www.google.com")

    # find the element that's name attribute is q (the google search box)
    inputElement = driver.find_element_by_name("q")

    # type in the search
    inputElement.send_keys("cheese!")

    # submit the form (although google automatically searches now without submitting)
    inputElement.submit()

    try:
        # we have to wait for the page to refresh, the last thing that seems to be updated is the title
        WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

        # You should see "cheese! - Google Search"
        print('Title: '.format(driver.title))
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
