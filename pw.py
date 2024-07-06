import os
from dotenv import load_dotenv

# pegar a senha do env
def get_pw():
    load_dotenv()
    return os.getenv('rootpw')
