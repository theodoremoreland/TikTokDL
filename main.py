# Third Party
from splinter import Browser

# Custom
from scripts.sanitizeConsoleLog import sanitizeLinks

downloadService = "https://musicallydown.com/"

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
browser.driver.set_window_size(1280, 720)

for link in sanitizeLinks():
    browser.visit(downloadService)
    while True:
        if browser.find_by_id('link_url').visible == True:
            inputField = browser.find_by_id('link_url')
            break
    inputField.fill(link)
    browser.find_by_name('submit').click()
    while True:
        if browser.links.find_by_partial_href('=mp4').visible == True:
            browser.links.find_by_partial_href('=mp4').click()
            break
    