import webbrowser, sys, pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#docs for selenium
#https://selenium-python.readthedocs.io/getting-started.html

#webbrowser is...
#sys is for the command line argument...

if len(sys.argv) > 1:
    address = ''.join(sys.argv[1:])
    print(address)
else:
    #get address from clipboard
    address = pyperclip.paste()

#webbrowser.open('https://www.google.com/maps/place/' + address)

#code for using selenium, make sure to download the library using pyenv
#make sure to install the driver for firefox, it's called geckobox
#link here - https://github.com/mozilla/geckodriver/releases/tag/v0.26.0

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_id("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()