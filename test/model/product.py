from test import db
from test.model.base import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = 'products'
    
    name = db.Column(db.String(128), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))

    def __repr__(self):
        return "<%s|%d: %s (%s)>" % (self.uuid, self.id, self.email, self.name)
