from model import Recipe


class TestRecipeFunctions:
    def testIfRecipeHasIngredients(self):
        recipe = Recipe.Recipe("Village Salad")
        recipe.ingredients = ["Tomato", "Cucumber", "Feta", "Olives"]
        assert recipe.hasIngrediets() == True;
