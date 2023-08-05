from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.2'
DESCRIPTION = 'API Wrapper for Kur.ac.'
LONG_DESCRIPTION = '''<p align="center">
  <img src="https://i.ibb.co/1vyfvn6/kurdotac.png" width="400"/>
 </p>
 
## What is kur.ac?
Kur.ac is a free to use URL shortener offering various custom subdomains.
A user can paste their URL, select a subdomain and get a shorter link.

The following subdomains are offered:
```koji```
```mali```
```oces```
```veliki```
```volim```

## Repository
This repository hosts an API wrapper made for this service.

The wrapper was made using only the requests Python library. It works by sending a POST request to [http://www.kur.ac/_generate](http://www.kur.ac/_generate).

## Installation and usage
In order to start shortening URLs using this package, you must first install it by running ```pip install kurac```.

After the installation is complete, you may import the package by typing ```import kurac``` into your Python console or adding it to your script. You may also import it by using ```from kurac import kurac```.

Finally, you may run the kurac function to generate a shortened URL. This function takes two arguments: *url* and *prefix*. The *url* argument is where you specify the link you'd like to shorten, and the prefix argument specifies the prefix to be appended. If left blank, the [kur.ac](kur.ac) service will automatically generate one.'''

# Setting up
setup(
    name="kurac",
    version=VERSION,
    author="i-vone",
    url="https://github.com/i-vone/kur.ac",
    author_email="paljetakos@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["requests"],
    keywords=["url shortener"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)