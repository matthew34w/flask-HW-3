
from __init__ import db, ma

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    
class CarSchema(ma.Schema):
    class Meta:
        fields = ('id', 'make', 'model', 'year')