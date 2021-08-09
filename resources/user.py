import sqlite3
from typing import Text
from flask_restful import Resource,reqparse 
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',type=str,required=True,help="The field username can't be blank")
    parser.add_argument('password',type=str,required=True,help="The field password can't be blank")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']) != None:
            return {"message": "User already exists."}, 400

        user = UserModel(data['username'],data['password'])
        user.save_to_db()
        return {"message": "User created successfully."}, 201

