
import mapnavlib
from mapnavlib.gestures.gesture import gesture
from mapnavlib.mapweb.open_browser import open_html_n_exec

def main():
    print(f"MapNavlib version: {mapnavlib.__version__}")
    # gesture()
    open_html_n_exec()


if __name__ == "__main__":
    main()
