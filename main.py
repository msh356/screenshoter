from time import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from flask import Flask, send_file
from datetime import datetime
import os

time_from_start = int(time())
print("""
░▄▀▀░▄▀▀▒█▀▄▒██▀▒██▀░█▄░█░▄▀▀░█▄█░▄▀▄░▀█▀▒██▀▒█▀▄
▒▄██░▀▄▄░█▀▄░█▄▄░█▄▄░█▒▀█▒▄██▒█▒█░▀▄▀░▒█▒░█▄▄░█▀▄ v1.0
New day, new adventures!

""")
print("All modules loaded!")

app = Flask(__name__)
print("Created Flask app")
service = Service()
driver = webdriver.Chrome(service=service)
print("Loaded service")

@app.route('/<path:page>')
def screenshot(page):
    if not page.startswith("http://") and not page.startswith("https://"):
        page = "http://" + page

    now = datetime.now()
    screenshot_name = now.strftime("./screenshots/%Y-%m-%d %H:%M:%S.png")
    
    driver.get(page)
    driver.save_screenshot(screenshot_name)

    return send_file(screenshot_name, mimetype='image/png')

print("Defined routes")

if __name__ == '__main__':
    time_for_start = int(time()) - time_from_start
    print("I am ready in " + str(time_for_start) + "s. Starting Flask app...")
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)

driver.quit()
