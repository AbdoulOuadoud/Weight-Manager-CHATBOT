
from dotenv import dotenv_values

environ = dotenv_values('.env')

API_KEY = environ.get('API_KEY', None)