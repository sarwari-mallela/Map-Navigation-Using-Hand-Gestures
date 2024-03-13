
import webbrowser
import os
import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def open_browser_with_file(browser_name, file_path):
    try:
        if browser_name == 'firefox':
            driver = webdriver.Firefox()
        elif browser_name == 'chrome':
            driver = webdriver.Chrome()
        elif browser_name == 'safari':
            driver = webdriver.Safari()
        else:
            print("Unsupported browser.")
            return False
        
        driver.get(f"file://{file_path}")
        return driver
    except Exception as e:
        print(f"Failed to open {browser_name}: {e}")
        return None

def wait_for_q_keypress():
    print("Press 'q' to quit.")
    keyboard.wait('q')

def execute_js(driver, script):
    try:
        driver.execute_script(script)
    except Exception as e:
        print(f"Failed to execute script: {e}")

html_file_path = "C:/Users/aleja/Documents/Python Scripts/cv/group/Map-Navigation-Using-Hand-Gestures/tests/mapmove_js.html"
js_script = "console.log('hello world');"

print("executing...")

# Try opening browsers in order
for browser in ['firefo x', 'chrome', 'safari']:
    driver = open_browser_with_file(browser, html_file_path)
    if driver:
        execute_js(driver, js_script)
        break
else:
    print("No supported browsers found.")

if driver:
    wait_for_q_keypress()
    driver.quit()