#!/usr/bin/python3
import sys
APPNAME='test0'
sys.path.insert(0,f'/var/www/{APPNAME}/')
sys.path.insert(0,f'/var/www/{APPNAME}/{APPNAME}/')

import logging
logging.basicConfig(stream=sys.stderr)

from test0 import app as application
