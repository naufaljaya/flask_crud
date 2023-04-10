from module import db
from datetime import datetime

class Todo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String(length=200), nullable=False)
    completed = db.Column(db.Integer(), nullable=False, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id