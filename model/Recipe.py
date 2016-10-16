class Recipe:
    title = ""
    type = ""
    description = ""
    ingredients = list()  # Create an empty list
    preparation = ""
    servings = 0
    time = 0

    recipeCount = 0

    def __init__(self, title):
        self.title = title
        Recipe.recipeCount += 1

    def hasIngrediets(self):
        return len(self.ingredients) > 0
