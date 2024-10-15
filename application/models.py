from .database import db  # Assuming db is defined in database.py

class User(db.Model):
    __tablename__ = "user_info"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    pincode = db.Column(db.Integer(), nullable=False)
    type = db.Column(db.String(), nullable=False, default="user")
    # professional = db.relationship("Professional", backref="user_info")

class Professional(db.Model):
    __tablename__ = "professional_info"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    service = db.Column(db.String(), nullable=False, unique=True)
    exp = db.Column(db.Integer())
    add = db.Column(db.String(), nullable=False)
    pin = db.Column(db.Integer(), nullable=False)
    type = db.Column(db.String(), nullable=True, default="professional")
    # service_info = db.relationship("Service", backref = "professional_info")
    # user_id = db.Column(db.Integer, db.ForeignKey("user_info.id", nullable = False))
    

class Service(db.Model):
    __tablename__ = "service_info"
    id = db.Column(db.Integer(), primary_key=True)
    service_name = db.Column(db.String(), nullable=False, unique=True)
    description = db.Column(db.String(), nullable=False)
    base_price = db.Column(db.Integer(), nullable=False)
    # professional_id = db.Column(db.Integer, db.ForeignKey("professional_info.id"), nullable = False)