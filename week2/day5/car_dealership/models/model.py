from database.index import db
from datetime import datetime

class Car(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(150), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(12,2), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
