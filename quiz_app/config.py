import os


class Config:
    SECRET_KEY = "Qh:w}n0DOrC1SI"
    SERVER_NAME = "localhost:81"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


