from application import db
from application.models import Members, Cars

db.drop_all()
db.create_all()