
import keyboard
from mapnavlib.gestures.gesture_detection import gest_dect
from shared_utils import SharedState

def main():
    shared_state = SharedState()

    # Set up a non-blocking key listener for 'q' to exit
    keyboard.add_hotkey('q', lambda: shared_state.set_exit_flag(True))

    # Directly call the gesture detection function
    # Note: This will block further code execution until it completes or an exit flag is set
    gest_dect(shared_state)

if __name__ == "__main__":
    main()
