import os
import sys
import asyncio
import shutil
from io import BytesIO
from functools import wraps
from textwrap import dedent
from random import choice, shuffle
from collections import defaultdict

import urllib.request


required = ["locmaker.py","locmaker_README.txt","Run.cmd"]

for item in required:
    print('Downloading '+item+'...')
    url = 'https://raw.github.com/Chupachu/LocMaker/master/'+item  
    urllib.request.urlretrieve(url, item)
optionals = ["countries.txt","ideologies.txt","out.yml"]

for item in optionals:
    if not os.path.isfile(item):
        print('Downloading '+item+'...')
        url = 'https://raw.github.com/Chupachu/LocMaker/master/'+item  
        urllib.request.urlretrieve(url, item)  