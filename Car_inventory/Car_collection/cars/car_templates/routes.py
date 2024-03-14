from flask import Blueprint, jsonify,request
from flask_login import login_required

from __init__ import db,ma,app
from car_templates.Car_Models import Car, CarSchema



auth = Blueprint('cars', __name__, template_folder='car_templates')



car_schema = CarSchema()
cars_schema = CarSchema(many=True)

@app.route('/cars', methods=['POST'])
@login_required
def create_car():
    make = request.json['make']
    model = request.json['model']
    year = request.json['year']
    new_car = Car(make=make, model=model, year=year)
    db.session.add(new_car)
    db.session.commit()
    return car_schema.jsonify(new_car)

@app.route('/cars', methods=['GET'])
@login_required
def get_cars():
    all_cars = Car.query.all()
    result = cars_schema.dump(all_cars)
    return jsonify(result)

@app.route('/cars/<id>', methods=['GET'])
@login_required
def get_car(id):
    car = Car.query.get(id)
    return car_schema.jsonify(car)