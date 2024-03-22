
import os
import webbrowser
import keyboard

def get_full_path(relative_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, relative_path)

def open_html_n_exec(shared_state):
    print("> Opening browser...")
    relative_path = 'mapmove.html'
    full_path = get_full_path(relative_path)

    # This will open the HTML file in the default browser
    webbrowser.open('file://' + full_path)

    print("Press 'q' to quit...")
    keyboard.wait('q')
    shared_state.set_exit_flag(True)