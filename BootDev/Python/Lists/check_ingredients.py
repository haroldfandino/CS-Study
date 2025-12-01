def check_ingredient_match(recipe, ingredients):

    missing_ingredients = []
    matched_ingredients = []

    for recipeIngredient in recipe:
        if recipeIngredient in ingredients:
            matched_ingredients.append(recipeIngredient)
        else:
            missing_ingredients.append(recipeIngredient)

    percentage = (len(matched_ingredients) * 100) / len(recipe)

    return percentage, missing_ingredients

recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
ingredients = ["Dragon Scale", "Phoenix Feather", "Troll Tusk"]

check_ingredient_match(recipe, ingredients)

# percentage, missing_ingredients = check_ingredient_match(recipe, ingredients)
# print(percentage, missing_ingredients)
# # Prints: 75.00 ["Unicorn Hair"]