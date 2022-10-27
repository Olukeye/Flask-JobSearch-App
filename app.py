from flask import Flask
from .database import  SessionLocal, Base, engine
from .config import settings
from . import user


Base.metadata.create_all(bind=engine)

app = Flask(__name__)


    
@app.route('/')
def index():
    return "Hello There guys, been a while and i'm getting lazy!!!!!!!!!"


if '__name__' == '__main__':
    app.run(debug = True)
    
    
    
    
    '''
    To auto-reload your app , you could use the command bellow
    'flask --app example_app.py --debug run'
    '''