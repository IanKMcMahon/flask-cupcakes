"""Flask app for Cupcakes"""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask-cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route('/api/cupcakes')
def show_all_cupcakes():

@app.route('/api/cupcakes/<int:cupcake_id>')
def show_cupcake_detail(cupcake_id)


@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():