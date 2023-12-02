"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask-cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


def serialize_cupcake(cupcake):
    """Serialize a dessert SQLAlchemy obj to dictionary."""

    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.calories,
        "rating": cupcake.rating,
        "img_url": cupcake.img_url
    }


@app.route('/api/cupcakes')
def show_all_cupcakes():

    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcake(c) for c in cupcakes]

    return jsonify(cupcakes=serialized)


@app.route('/api/cupcakes/<int:cupcake_id>')
def show_cupcake_detail(cupcake_id):

    cupcake_id = Cupcake.query.get(cupcake_id)


@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():

    flavor = request.json["name"]
    size = request.json["calories"]
    rating = request.json["rating"]
    img_url = request.json["img_url"]

    new_cupcake = Cupcake(
        flavor=flavor,
        size=size,
        rating=rating,
        img_url=img_url)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = serialize_cupcake(new_cupcake)

    return (jsonify(cupcake=serialized), 201)
