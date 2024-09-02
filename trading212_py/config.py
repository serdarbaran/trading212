import os
from dotenv import dotenv_values
import configparser

config = configparser.ConfigParser()
config.read(filenames='trading212_py/T212.INI')

MODULE_NAME: str = config.get('DEFAULT','NAME')
API_VERSION: str = config.get('GENERAL', 'API_VERSION')


InProduction = True
if os.getenv('IN_PRODUCTION', 'false') == 'false':
    # Load environment variables from .env/.secret or .env/.shared
    # Specify the path to the .env file if needed
    env_config = {
        **dotenv_values(dotenv_path=".env/.shared"),  # load shared development variables
        **dotenv_values(dotenv_path=".env/.secret"),  # load sensitive variables
        **os.environ,  # override loaded values with environment variables
    }
    InProduction = False
else: pass

ACCOUNT_TYPE= env_config.get('ACCOUNT_TYPE', 'live')
API_KEY= env_config.get('T212_API_KEY', None)