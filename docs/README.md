## Map Navigation Using Hand Gestures

![Static Badge](https://img.shields.io/badge/version-0.1-orange)
![Static Badge](https://img.shields.io/badge/python-3.9-blue)

Pan, zoom and click through Google Maps using 1 hand gestures in real time.

![Gif of repo in action](./gif.gif)

### Dependencies
[MediaPipe](https://developers.google.com/mediapipe) for high-fidelity tracking of the hand.

[OpenCV](https://opencv.org/) for camera video capture.

[Folium](https://python-visualization.github.io/folium/latest/) for HTML Leaflet map visualization.

[Keyboard](https://github.com/boppreh/keyboard) for OpenCV camera and browser kill control.

[IPython](https://ipython.org/) for ipynb test notebooks.

[Python 3.9](#) was used due to MediaPipe having reports of compatibility issues, particularly with Windows and Python 3.11 [(Mediapipe issue #3849)](https://github.com/google/mediapipe/issues/3849)

### Compile and run

```bash
# Clone repository
$ git clone https://github.com/sarwari-mallela/Map-Navigation-Using-Hand-Gestures

# If needed
$ conda create -n mapnav python=3.9

# Install project config
$ python setup.py install

# Start python http server on a free port
$ python -m http.server 8000

# On another terminal, execute the main script
$ python .\main.py
```

Open your preferred browser at: http://localhost:8000/mapnavlib/mapweb/mapmove.html

For ease of use we recommend positioning the OpenCV camera and browser like the gif seen above.

### Contributing/License

Fork it, modify it, push it, eat it, summon a duck god with it. Whatever resonable day-to-day activity you prefer ( •ᴗ•)b