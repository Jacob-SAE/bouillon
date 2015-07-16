from bouillon import db
from bouillon.model.base import Base
from sqlalchemy.orm import relationship

class Pool(Base):
    __tablename__ = 'pools'
    
    name = db.Column(db.String(128), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))

    def __repr__(self):
        return "<%s|%d:poolname=%s >" % (self.uuid, self.id, self.name)
