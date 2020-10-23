import config 

from flask import Flask
from flask_cors import CORS

from sqlalchemy  import create_engine 

def create_app():
    app = Flask(__name__) # Flask를 객체화, 인스턴스를 app변수에 저장 
    app.debug = True
    app.json_encoder = CustomJSONEncoder

    app.config.from_pyfile('config.py') # config 설정
    
    database = create_engine(app.config['DB_URL'],encoding = 'utf-8',max_overflow = 0) #DB연결
    app.databse = database 

    CORS(app, resources={r'*' : {'origins':'*'}}) #CORS 설정

    return app