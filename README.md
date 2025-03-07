# Screenshoter ![badge](https://badgen.net/badge/version/1.1)
Screenshoter - is VERY simple web screenshoter, using Python, Selenium and Flask. It's my first public project. This program makes an API, where you can enter web page and get it's screenshot. **Warning: Project is very unsecure and unstable.**
## Installing
    git clone https://github.com/msh356/screenshoter
    cd screenshoter
    python3 -m venv env
    source ./env/bin/activate
    pip install flask selenium waitress
You also need to be `chromedriver`, `geckodriver` or any other web driver installed on your system.
## Using
In first, we need to start:

    source ./env/bin/activate
    python3 main.py
Then we can use any instrument to use Screenshoter:
## Adding to banlist
First, cd to Screenshoter directory

    cd ~/screenshoter
Then, we need to open banned.list with any editor you'd like

    nano banned.list
Prompt URL you want to add to the banlist, **STARTING WITH http://!!! ANY URL, NOT STARTING FROM http://, WILL BE IGNORED!**

    http://example.com
Save file and exit
*P.S. If you want to ban chrome:// urls, don't worry, code bug is helping you.*
### wget
    wget http://localhost:8080/example.com
### curl
    curl -o example.png http://localhost:8080/example.com
## Known issues
* When using a normal human web browser to get webpage, browser also trying to get favicon, and server trying to request favicon.ico.