#!/usr/bin/python3
import sys
sys.path.insert(0,'/var/www/test0/')
sys.path.insert(0,'/var/www/test0/test0/')

import logging
logging.basicConfig(stream=sys.stderr)

from test0 import app as application
