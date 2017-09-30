import os
basedir = os.path.abspath(os.path.dirname(__file__))

env = dict(
	host = '0.0.0.0',
	port = 4000,
	user = 'root',
	password = 'team1'
	db = 'cfg')

class Config(object):
    DEBUG = True
    SECRET_KEY = '3713CCDFEF818733AE46E3545B613'