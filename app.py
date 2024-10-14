from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shows.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return "Welcome to the late show!!"

if __name__ == "__main__":
    app.run(debug=True)
