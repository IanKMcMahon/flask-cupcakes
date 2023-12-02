"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG_URL = "https://tinyurl.com/demo-cupcake"


class Cupcake(db.Model):
    """cupcakes"""

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.String, nullable=False)
    size = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    img_url = db.Column(db.String, nullable=False, default=DEFAULT_IMG_URL)


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.connect_all(app)
