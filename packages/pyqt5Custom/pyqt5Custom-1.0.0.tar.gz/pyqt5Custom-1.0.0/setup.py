from setuptools import setup, find_packages
import os

_ROOT = os.path.abspath(os.path.dirname(__file__))
def get_data(path):
    return os.path.join(_ROOT, path)

setup(
    name="pyqt5Custom",
    packages = find_packages(),
    #data_files=[('libs', ['keys.py', "terminal.py"]), ('', ['favicon.png'])],
    include_package_data=True,
    version="1.0.0",
    author="Kadir Aksoy",
    author_email="kursatkadir014@gmail.com",
    description="More useful widgets for PyQt5",
    url="https://github.com/kadir014/pyqt5-custom-widgets",
    project_urls={
    'Documentation': 'https://github.com/kadir014/pyqt5-custom-widgets/blob/main/documentation.md',
    },
    keywords='gui ui pyqt widget',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
                      "PyQt5",
                      "requests"
                      ]
)
