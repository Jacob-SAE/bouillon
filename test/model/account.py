from test import db
from test.model.base import Base
from sqlalchemy.orm import relationship

class Account(Base):
    __tablename__ = 'accounts'
    
    first_name = db.Column(db.String(128), nullable=False)
    middle_initial = db.Column(db.String(128), nullable=True)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)

    pools = relationship("Pool", order_by="Pool.id", backref="house")

    def __repr__(self):
        return "<%s|%d || %s %s. %s --%s>" % (self.uuid, self.id, self.first_name, self.middle_initial, self.last_name, self.email)
