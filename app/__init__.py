from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "d4d68adfc046579d752916505b72d581"
    
    return app