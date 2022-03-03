from ast import Delete
import mimetypes
from flask import Response, request
from database.models import Recipe
from flask_restful import Resource


# Get
class RecipesApi(Resource):
    def get(self):
        recipes = Recipe.objects().to_json()
        return Response(
            recipes,
            mimetype = "application/json"
        )
# Create
    def post(self):
        body = request.get_json()
        recipe = Recipe(**body).save()
        id = recipe.id
        return {"id": str(id)}

# Update
class RecipeApi(Resource):
    def put(self,id):
        body = request.get_json()
        Recipe.objects.get(id = id).update(**body)
        return ''
# Delete
    def delete(self,id):
        recipe = Recipe.objects.get(id = id).delete()
        return ''

    def get(self,id):
        recipes = Recipe.objects.get(id = id).to_json()
        return Response(recipes, mimetype = "application/json") 
