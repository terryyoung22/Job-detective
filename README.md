# Jobdetective
Your personal job finder bundled in a single container

# Future Enhancements
- Scrape for links `ahref` class
- Scrape linkedin, Dice, Monster
- included links I use for Automation in AWS and crons locally

# Variables Needed:
* emailcsv.py
    - emailfrom
    - emailto
    - fileToSend
    - username
    - password
    - serverg
    - port

* jobDetective.py
    - joblink

# Install!
Install is simple! After you fill in needed variables, you can either:
 - `Docker build` the dockerfile and run the container, or just use the `localContainerBuild.sh` and change the name of the image
 - Or just run it locally if you have the dependices already installed (I am lazy yes, I will be adding the requirements.txt)
* If running locally, move `macdriver` or which ever you need to `usr/local/bin` or wherever `$PATH` can be called
* Add these libraries for scraping:
    - python3 -m pip install wheel pandas BeautifulSoup4 awscli
        - awscli
        - selenium
        - pandas
        - bs4 (beautifulsoup)


# Helpful Links
* Chrome Drivers [Drivers](https://chromedriver.chromium.org/downloads)
* Errors for pandas [panda](https://stackoverflow.com/questions/33481974/importerror-no-module-named-pandas)
* Install Chromium ubuntu [Install](https://stackoverflow.com/questions/58997430/how-to-install-chromium-in-docker-based-on-ubuntu-19-10-and-20-04)
* Get Chrome driver for Unbuntu [linuxdriver](https://www.srcmake.com/home/selenium-python-chromedriver-ubuntu)
* Selenium driver crash [error](https://stackoverflow.com/questions/53073411/selenium-webdriverexceptionchrome-failed-to-start-crashed-as-google-chrome-is)
* linux driver chrome repo [REPO](http://chromedriver.storage.googleapis.com/index.html)
* Find href links - If you wanna try! [links!](https://stackoverflow.com/questions/34759787/fetch-all-href-link-using-selenium-in-python)
* google captcha for container [captcha](https://accounts.google.com/b/0/DisplayUnlockCaptcha)
^ Good for if you are having permissions issues with chrome
* Genereate app PW [app](https://support.google.com/domains/answer/9437157)

# CONTACT ME!
Feel free to email and let me know what you think of this! Its still in baby stages and I stripped a good portion down for security reasons but first "big"
open source project! Lay it on me, all criticism welcomed!

Email: terryyoung1192@gmail.com