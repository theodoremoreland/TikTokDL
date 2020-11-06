# TikTokDL
This project was created to automate the process of going through a TikTok profile's entire library of public videos and downloading them. The project was created as an emergency method in lieu of the United States government announcing that the app would no longer be available through app stores. Because these scripts were written the night before the app was removed from app stores, I am unable to entirely demonstrate how the scripts and process worked. Fortunately, there isn't much to it, so I will simply describe the process below.  

The process below assumes some familiarity with programming, such as how to use a web browser's development console and how to execute a Python script. I'm making this assumption on the grounds that the scripts aren't important enough to actually run and/or will likely be outdated in a short time. The explanation below is moreso to get a basic idea of this project. Note: TikTok has a feature that tries to make it hard for bots to scrape their site, so I had to find a quick and dirty workaround which led to more of a "semi-automated" process as opposed to being completely automated.

## Process (using a web browser)
* First, the user visits their desired user profile.
* Then the user clicks on said profile's first video.
* Now the user must confirm that browser window is at least 1280px by 720px, if not, reload page (a clickable arrow shaped button for alternating videos must be visible. That arrow is what the scripts use to automate cycling through the videos).
* Next the user copies and pastes the "pasteInConsole" script into web browser's dev console.
* Once pasting the script, execute the script by pressing the 'Enter' key while in the dev console.
* The script will then automatically cycle through the user profile and print links to each video in the console. Copy and paste said links into a "links.txt" file (view "links.txt.example to see what logs and links.txt should look like").
* Now execute the "main.py" script and the script will visit a second website to then download each of the user's videos

*Thank you for your interest.*