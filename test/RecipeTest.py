import unittest

from model import Recipe


class TestRecipeFunctions(unittest.TestCase):
    def testIfRecipeHasIngredients(self):
        recipe = Recipe.Recipe("Village Salad")
        recipe.ingredients = ["Tomato", "Cucumber", "Feta", "Olives"]

        self.assertTrue(recipe.hasIngrediets())