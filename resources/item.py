from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help="The field can't be blank")
    parser.add_argument('store_id',type=int,required=True,help="Every Item needs a store id")
    
    @jwt_required()
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(),200         # item is an object must return json 
        return {'message': 'Item does not exist'},404

    def post(self,name):
        if ItemModel.find_by_name(name):
            return {'message': "an item with name '{}' already exists".format(name)},400

        data = Item.parser.parse_args()
        item=ItemModel(name,data['price'],data['store_id'])  
        try: 
            item.save_to_db()
        except Exception as e:
            print(e)
            return {"message": "An error occured inserting item"},500

        return item.json(),201

    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name) 
        if item is None:
            item = ItemModel(name,data['price'],data['store_id'])  #could be **data to pass arguments
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {'message':'Item deleted'}
        

class ItemList(Resource):
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}   #List comprehension