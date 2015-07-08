from .base import *

try:
	from .local import *
	live = False
except:
	live = True

if live is True:
	from .production import *