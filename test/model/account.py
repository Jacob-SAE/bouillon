from test import db
from test.model.base import Base
from sqlalchemy.orm import relationship

class Account(Base):
    __tablename__ = 'accounts'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)

    def __repr__(self):
        return "<%s|%d: %s (%s)>" % (self.uuid, self.id, self.email, self.name)
