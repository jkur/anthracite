import os
import sys

import os.path
os.chdir(os.path.dirname(__file__))


#site.addsitedir('/srvanthracite/')
sys.path.append('/srv/anthracite')

import bottle
from anthracite import app


#application = bottle.default_app()
application = app
