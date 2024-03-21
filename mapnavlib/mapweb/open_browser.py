
import os
import threading
import keyboard
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

def get_full_path(relative_path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, relative_path)

def start_server(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    try:
        # Change the current working directory to make server work
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print(f"Starting httpd server on port {port}")
        httpd.serve_forever()
    except Exception as e:
        print(f"Failed to start server: {e}")

def open_html_n_exec(shared_state, port):
    print("> Opening browser...")
    relative_path = 'mapmove.html'
    full_path = get_full_path(relative_path)
    directory = os.path.dirname(full_path)

    # Start the server in a separate thread
    # Server will keep running in daemon mode until the main program exits
    server_thread = threading.Thread(target=start_server, args=(HTTPServer, lambda *args, directory='.', **kwargs: SimpleHTTPRequestHandler(*args, directory=directory, **kwargs), port,))
    server_thread.daemon = True
    server_thread.start()

    # Opening browser with html file
    url = f"http://localhost:{port}/{os.path.basename(relative_path)}"
    webbrowser.open_new(url)

    keyboard.wait('q')
    shared_state.set_exit_flag(True)