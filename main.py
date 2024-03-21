
import threading
import keyboard
import requests
import mapnavlib
from mapnavlib.gestures.gesture_detection import gest_dect
from mapnavlib.mapweb.open_browser import open_html_n_exec
from shared_utils import SharedState

def check_server_is_running(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

def main():
    shared_state = SharedState()
    print(f"> MapNavlib version: {mapnavlib.__version__}")

    # Create threads for gesture detection and opening the browser
    gesture_thread = threading.Thread(target=gest_dect, args=(shared_state,))
    browser_thread = threading.Thread(target=open_html_n_exec, args=(shared_state,))

    # Start the threads
    # gesture_thread.start()
    browser_thread.start()

    # Quick check
    if check_server_is_running('http://localhost:1234'):
        print(">>> Server is: running")
        print("Press 'q' to quit")
    else:
        print(">>> Server is: not running")

    # Set up a non-blocking key listener
    keyboard.add_hotkey('q', lambda: shared_state.set_exit_flag(True))

    # Wait for both threads to complete
    gesture_thread.join()
    browser_thread.join()

if __name__ == "__main__":
    main()
