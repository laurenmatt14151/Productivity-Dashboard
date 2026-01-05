'''
Configuration settings for database connection.
'''

import os # Library needed to access token from environment variables
from dotenv import load_dotenv # Load environment variables from .env file

load_dotenv() # Load token from .env file

'''
Database configuration settings
If productivity.db file does not exist, it will be created
'''
DB_URL = 'productivity.db' # Database file name

'''

'''