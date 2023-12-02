"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.app_context().push()

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

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())


@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():

    flavor = request.json["flavor"]
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


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def edit_cupcake(cupcake_id):

    data = request.json
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.img_url = data['img_url']

    cupcake_id = Cupcake.query.get(cupcake_id)

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def remove_cupcake(cupcake_id):
    """Delete cupcake"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")
