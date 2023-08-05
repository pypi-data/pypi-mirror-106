import setuptools
import os
import codecs

with open("README.rst", "r", encoding="utf-8") as readme:
    long_description = readme.read()

# https://packaging.python.org/guides/single-sourcing-package-version/
def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setuptools.setup(
    name = "fish_pen",
    version = get_version("fish_pen/__init__.py"),
    author = "Fisherman's Friend",
    author_email = "fish@waifu.club",
    description = "Package for demonstration purposes in documentation",
    long_description = long_description,
    long_description_content_type = "text/x-rst",
    url = "https://gitgud.io/fish/fish-pen",
    project_urls = {
        "Documentation":    "https://fish-pen.readthedocs.org",
        "Source":           "https://gitgud.io/fish/fish-pen"
    },
    classifiers = [
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    packages = [
        "fish_pen"
    ]
)
