from test import db
from test.model.base import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    account = db.relationship('Account', backref=db.backref('products', lazy='dynamic'))

    def __repr__(self):
        return "<%s|%d: %s (%s)>" % (self.uuid, self.id, self.email, self.name)
