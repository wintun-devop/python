import os
from dotenv import load_dotenv

#to get to ensure from .env
load_dotenv(override=True)
#get from system
# path = os.environ["PATH"]
#env_from_system = os.getenv("APP_API_KEY")

env_from_app = os.getenv("MY_KEY")
print(env_from_app)

