from db import db


class StoreModel(db.Model):
    __tablename__="stores"                         # SQLALCHEMY
    id = db.Column(db.Integer,primary_key=True)   # SQLALCHEMY
    name = db.Column(db.String(80))               # SQLALCHEMY

    items = db.relationship('ItemModel',lazy='dynamic')

    def __init__(self, name):
        self.name = name
    
    def json(self):
        return {'name':self.name,'items':[item.json() for item in self.items.all()]} 

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()  # SQLALCHEMY

    def save_to_db(self):                              # SQLALCHEMY will add or update
        db.session.add(self)                           # SQLALCHEMY
        db.session.commit()                            # SQLALCHEMY

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()                            # SQLALCHEMY

