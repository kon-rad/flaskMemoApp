import os
from app import db, create_app
from app import models

app = create_app(config_name=os.getenv('APP_SETTINGS'))

if __name__ == '__main__':
    manager.run()