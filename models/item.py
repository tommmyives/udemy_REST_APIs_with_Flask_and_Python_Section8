from db import db


class ItemModel(db.Model):
    __tablename__="items"                         # SQLALCHEMY
    id = db.Column(db.Integer,primary_key=True)   # SQLALCHEMY
    name = db.Column(db.String(80))               # SQLALCHEMY
    price = db.Column(db.Float(precision=2))      # SQLALCHEMY
    store_id = db.Column(db.Integer,db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')


    def __init__(self, name, price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
    
    def json(self):
        return {'name':self.name,'price':self.price} 

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()  # SQLALCHEMY

    def save_to_db(self):                              # SQLALCHEMY will add or update
        db.session.add(self)                           # SQLALCHEMY
        db.session.commit()                            # SQLALCHEMY

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()                            # SQLALCHEMY

