from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from config import Config 
from dotenv import load_dotenv 
 
load_dotenv() 
db = SQLAlchemy() 
 
def create_app(): 
    app = Flask(__name__) 
    app.config.from_object(Config) 
     
    db.init_app(app) 
     
    from routes.auth import auth_bp 
    from routes.events import events_bp 
    from routes.registrations import reg_bp 
     
    app.register_blueprint(auth_bp, url_prefix='/api') 
    app.register_blueprint(events_bp, url_prefix='/api') 
    app.register_blueprint(reg_bp, url_prefix='/api') 
     
    with app.app_context(): 
        db.create_all() 
     
    return app 
 
app = create_app() 
 
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000, debug=True) 


python app.py 
