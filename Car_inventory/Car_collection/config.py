import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('postgresql://ytxdurpb:8SeN2cjLygPzwgcvs2aY5NaNs5-xHTCS@ruby.db.elephantsql.com/ytxdurpb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False