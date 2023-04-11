# TODO - Create SQLAlchemy DB and Movie model

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the SQLAlchemy object
    db.init_app(app)

    ...

    class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Movie(id={self.id}, title='{self.title}', director='{self.director}', rating={self.rating})"

      from app import db

# Define the Movie model here

db.create_all()
