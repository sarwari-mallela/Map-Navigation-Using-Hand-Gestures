
import threading

class SharedState:
    def __init__(self):
        self._exit_flag = False
        self._lock = threading.Lock()

    def set_exit_flag(self, value):
        with self._lock:
            self._exit_flag = value

    def should_exit(self):
        with self._lock:
            return self._exit_flag