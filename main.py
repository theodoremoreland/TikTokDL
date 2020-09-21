# Visit desired user profile.
# Click on user's first video.
# Confirm that browser window is at least 1280px by 720px, if not, reload page (a clickable arrow shaped button for alternating videos must be visible)
# Copy and paste "pasteInConsole" script into web browser's dev console.
# Execute script (e.g. press 'Enter' after pasting "pasteInConsole" script)
# Copy and paste links logged in dev console into "links.txt" (view "links.txt.example to see what logs and links.txt should look like")
# Run "main.py"

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
    