
class Config:
    CSRF_ENABLED = True
    CORS_HEADERS = 'Content-Type'
    SECRET_KEY = '5791628bb034dfe0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/flask_api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False