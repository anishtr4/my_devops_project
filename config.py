class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:your_password@localhost/devops_project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'