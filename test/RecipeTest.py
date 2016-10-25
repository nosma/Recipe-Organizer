import unittest

from model import Recipe


class TestRecipeFunctions(unittest.TestCase):
    def testIfRecipeHasIngredients(self):
        recipe = Recipe.Recipe("Village Salad")
        recipe.ingredients = ["Tomato", "Cucumber", "Feta", "Olives"]
        self.assertTrue(recipe.hasIngrediets())

    def testIfRecipeHasPreparation(self):
        tomato_salad = Recipe.Recipe("Tomato Salad")
        tomato_salad.preparation = ["Wash tomatoes", "Cut tomatoes", "Eat tomatoes"]
        self.assertTrue(tomato_salad.hasPreparation())
