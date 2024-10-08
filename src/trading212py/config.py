import os
from dotenv import dotenv_values

# Set Trading212 API version
API_VERSION:str = 'v0'

InProduction = True

if os.getenv('IN_PRODUCTION', 'false') == 'false':
    # Load environment variables from .env/.secret or .env/.shared
    # Specify the path to the .env file if needed
    env_config = {
        **dotenv_values(dotenv_path=".env/.shared"),  # load shared development variables
        **dotenv_values(dotenv_path=".env/.secret"),  # load sensitive variables
        **os.environ,  # override loaded values with environment variables
    }
    # Set InProduction to False if not in production
    InProduction = False
else: pass

# Get the API key based on the account type
ACCOUNT_TYPE:str= env_config.get('ACCOUNT_TYPE', 'live')
API_KEY:str = env_config.get('T212_DEMO_API_KEY', None) if ACCOUNT_TYPE == 'demo' else env_config.get('T212_API_KEY', None)