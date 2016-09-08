import sys
sys.path.insert(0, '/var/www/html/python')
sys.stdout = sys.stderr
from provision import app as application