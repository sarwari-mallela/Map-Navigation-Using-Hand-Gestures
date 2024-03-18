
import os
import keyboard
from selenium import webdriver

def get_full_path(relative_path):
    # Get the directory of the current file (__file__ is the path to the current script)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path by joining the current directory with the relative path
    return os.path.join(current_dir, relative_path)

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

def execute_js(driver, file_path):
    try:
        with open(file_path, 'r') as js_file:
            js_script = js_file.read()
        driver.execute_script(js_script)
    except Exception as e:
        print(f"Failed to execute script from {file_path}: {e}")

def open_html_n_exec(shared_state):
    html_path = get_full_path('mapmove_js.html')
    js_path = get_full_path('maps_controller.js')
    print("Opening browser...")

    for browser in ['firefox', 'chrome', 'safari']:
        driver = open_browser_with_file(browser, html_path)
        if driver:
            execute_js(driver, js_path)
            break
    else:
        print("No supported browsers found.")

    if driver:
        print("Press 'q' to quit")
        keyboard.wait('q')
        shared_state.set_exit_flag(True)
        driver.quit()