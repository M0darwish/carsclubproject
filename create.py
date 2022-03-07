from application import db
from application.models

db.drop_all()
db.create_all()