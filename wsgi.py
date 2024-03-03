# wsgi v1.1:
#   Changed application path in /var/www/

# Bridging Python web application to Apache server using Web Server Gateway Interface
import sys
sys.path.insert(0,"/var/www/red-wire/")
from red_wire_app import server as application
