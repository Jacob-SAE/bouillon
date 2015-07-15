from test import db
from test.model.base import Base
from sqlalchemy.orm import relationship

class Account(Base):
    __tablename__ = 'accounts'
    
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    full_name = first_name + last_name
    email = db.Column(db.String(128), nullable=False, unique=True)
    

    products = relationship("Product", backref="account")

    def __repr__(self):
        return "<%s|%d: %s (%s)>" % (self.uuid, self.id, self.email, self.name)
