import os

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///.instance/sqlite.db')