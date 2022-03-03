from .db import db

class Recipe(db.Document): 
    name = db.StringField(required=True, unique=True)
    cuisine_type = db.StringField(required=True)
    description = db.StringField(required=True)
    image = db.StringField (required=True)
    ingredient_one = db.StringField(required=True)
    ingredient_two = db.StringField(required=False)
    ingredient_three = db.StringField(required=False)
    ingredient_four = db.StringField(required=False)
    ingredient_five = db.StringField(required=False)
    ingredient_six = db.StringField(required=False)
    ingredient_seven = db.StringField(required=False)
    directions = db.StringField(required =True)