import unittest

from model import Recipe


class TestRecipeFunctions(unittest.TestCase):
    def testIfRecipeHasIngredients(self):
        recipe = Recipe.Recipe("Village Salad")
        recipe.ingredients = ["Tomato", "Cucumber", "Feta", "Olives"]

        self.assertEquals(1, recipe.recipeCount)
        self.assertTrue(recipe.hasIngrediets())
        self.assertEquals(4, len(recipe.ingredients))
