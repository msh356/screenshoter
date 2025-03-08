from time import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from flask import Flask, send_file
from datetime import datetime
import os
from modules.properties_parser import parse

time_from_start = int(time())
print("""
░▄▀▀░▄▀▀▒█▀▄▒██▀▒██▀░█▄░█░▄▀▀░█▄█░▄▀▄░▀█▀▒██▀▒█▀▄
▒▄██░▀▄▄░█▀▄░█▄▄░█▄▄░█▒▀█▒▄██▒█▒█░▀▄▀░▒█▒░█▄▄░█▀▄ v1.2
New day, new adventures!

""")
print("All modules loaded!")

config_raw = open("server.properties")
config = config_raw.read()
config = parse(config)
config_raw.close()

print("Config imported!")
print(config)

index_raw = open("pages/index.html")
index = index_raw.read()
index_raw.close()
print("Index page loaded!")

banned_raw = open("banned.list")
banned = banned_raw.read().split("\n")
banned_raw.close()

print("Loaded banlist")

app = Flask(__name__)
print("Created Flask app")
service = Service()
driver = webdriver.Chrome(service=service)
print("Loaded service")

@app.route('/<path:page>')
@app.route('/')
def screenshot(page=None):
    try:
        if not page.startswith("http://") and not page.startswith("https://"):
            page = "http://" + page
    except AttributeError:
        if config["send_service_pages_as"] == "html":
            return index
        elif config["send_service_pages_as"] == "image":
            page = "file://" + os.path.dirname(os.path.abspath(__file__)) + "/pages/index.html"
    
    now = datetime.now()
    screenshot_name = now.strftime("./screenshots/%Y-%m-%d %H:%M:%S.png")
    
    if page in banned:
        page = "file://" + os.path.dirname(os.path.abspath(__file__)) + "/pages/banned.html"
    
    
    driver.get(page)
    driver.save_screenshot(screenshot_name)

    return send_file(screenshot_name, mimetype='image/png')

print("Defined routes")

if __name__ == '__main__':
    time_for_start = int(time()) - time_from_start
    print("I am ready in " + str(time_for_start) + "s. Starting Flask app...")
    from waitress import serve
    serve(app, host="0.0.0.0", port=config["port"])

driver.quit()
