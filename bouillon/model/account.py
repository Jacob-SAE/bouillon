from bouillon import db
from bouillon.model.base import Base
from sqlalchemy.orm import relationship


class Account(Base):
    __tablename__ = 'accounts'
    
    first_name = db.Column(db.String(128), nullable=False)
    middle_initial = db.Column(db.String(128), nullable=True)
    last_name = db.Column(db.String(128), nullable=False)
    stripe_token = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    city = db.Column(db.String(64), nullable=True)
    state = db.Column(db.String(64), nullable=True)
    phone = db.Column(db.String(16), nullable=True)
    username = db.Column(db.String(128), nullable=True)
    password = db.Column(db.String(128), nullable=True)

    pools = relationship("Pool", order_by="Pool.id", backref="house")

    def __repr__(self):
        return "<%s|%d || %s %s. %s --%s>" % (self.uuid, self.id, self.first_name, self.middle_initial, self.last_name, self.email)
