"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG_URL = "https://tinyurl.com/demo-cupcake"


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """cupcakes"""


__tablename__ = "cupcakes"

id = db.Column(
    db.Integer,
    primary_key=True)

flavor = db.Column(
    db.Text,
    nullable=False)

size = db.Column(
    db.Text,
    nullable=False)

rating = db.Column(
    db.Float,
    nullable=False)

image_url = db.Column(
    db.Text,
    nullable=False,
    default=DEFAULT_IMG_URL
)
