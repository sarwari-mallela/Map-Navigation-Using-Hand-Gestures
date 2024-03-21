
from setuptools import setup, find_packages
from pathlib import Path

# version
here = Path(__file__).absolute().parent
version_data = {}
with open(here.joinpath("mapnavlib", "__init__.py"), "r") as f:
    exec(f.read(), version_data)
version = version_data.get("__version__", "0.0")

install_requires = [
    "matplotlib==3.8.3"
    , "mediapipe==0.10.11"
    , "folium==0.16.0"
    , "keyboard==0.13.5"
    , "ipykernel==6.29.3"
    , "ipython==8.18.1"
    , "ipywidgets==8.1.2"
]

setup(
    name="mapnavlib"
    , version=version
    , install_requires=install_requires
    , package_dir={"mapnavlib": "mapnavlib"}
    , python_requires=">=3.9, <3.10"
    , packages=find_packages(where=".", exclude=["docs", "tests"])
)
