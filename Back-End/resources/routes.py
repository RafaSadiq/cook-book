from .recipe import RecipeApi, RecipesApi

def initialize_routes(api):
    api.add_resource(RecipesApi, "/api/recipes")
    api.add_resource(RecipeApi, "/api/recipes/<id>")

