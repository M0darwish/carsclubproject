from application import db
from application.models import Members

db.drop_all()
db.create_all()