import os

MONGODB_URL = os.environ['MONGO_URI']
MONGODB_DB_NAME = "car_rental"
MAX_CONNECTIONS_COUNT = 10
MIN_CONNECTIONS_COUNT = 1
JWT_TOKEN_PREFIX = "Token"
SECRET_KEY = "4E8D16A9BDD82A574F4DB7C1E3AB4"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # one week
