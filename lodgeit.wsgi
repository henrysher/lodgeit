# Example lodgeit file
import os
import sys
sys.path.append(os.path.dirname(__file__))
from lodgeit import make_app

application = make_app(
    # the path to the database
    dburi='sqlite:////tmp/lodgeit.db',
    # generate with os.urandom(30)
    secret_key='\x05\x82bgI\x99\xaay\xa5o\xef\xac\xa1\x93>Db\x04\xf1\x8b|\x7fT\x87|]LcM\x9d'
)
