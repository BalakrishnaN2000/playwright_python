import configparser
from dotenv import load_dotenv
import os


config = configparser.ConfigParser()
config.read(r'D:\playwright_python\playwright_python\resources\config\config.properties')
# print(config.sections())
# print(config.get('DEFAULT', 'browser'))

browser = config['DEFAULT']['browser'].strip().lower()
headless = config['DEFAULT']['headless'].strip().lower() == 'true'
url = config['DEFAULT']['url']

# print(config['DEFAULT']['url'])


# load_dotenv()
# config_path = os.getenv('CONFIG_PATH')
# print(config_path)

# Export the values to be accessed
__all__ = ['browser', 'headless', 'url']