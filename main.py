
import threading
import mapnavlib
from mapnavlib.gestures.gesture_detection import gest_dect
from mapnavlib.mapweb.open_browser import open_html_n_exec

def main():
    print(f"MapNavlib version: {mapnavlib.__version__}")

    # Create threads for gesture detection and opening the browser
    gesture_thread = threading.Thread(target=gest_dect)
    browser_thread = threading.Thread(target=open_html_n_exec)

    # Start the threads
    gesture_thread.start()
    browser_thread.start()

    # Wait for both threads to complete
    gesture_thread.join()
    browser_thread.join()

if __name__ == "__main__":
    main()
