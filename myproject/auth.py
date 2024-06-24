from flask import Blueprint, render_template, request, flash, jsonify
import requests


auth = Blueprint('auth', __name__)


SPOONACULAR_API_KEY = '9e399fbe5fd64a6d8608c41a3701fe35'

@auth.route('/steps')
def steps():
    steps = [
        {"text": "Step 1: Separate beef into 4 equal portions. Use hands to lightly form into patties the size of your buns."},
        {"text": "Step 2: Season generously with salt and pepper on both sides.", "underline": ["Season"], "gif": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZHZ6aXRpbm96azhranRoOWlzNnZ4bHoxa2UwdnB6bWFkbWwycDF3byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l4Jz3a8jO92crUlWM/giphy.gif"},
        {"text": "Step 3: Heat 1 tbsp oil in a heavy based skillet or BBQ over high heat. Add onion and cook until wilted and caramelised. Season with salt and pepper, then remove."},
        {"text": "Step 4: Heat 1 tbsp oil until smoking. Add patties and cook for 2 minutes until deep golden with a great crust. Cover with lid and cook for further 1 minute until cheese is melted."},
        {"text": "Step 5: Meanwhile, toast the cut side of the buns lightly.", "underline": ["toast"], "gif": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTVlanQ1M2lvdHBmd245a2kwN3Ryd2RsZmcxbGo2eDhocms4czl2aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/eEtcTm7xuF7nq/giphy.gif"},
        {"text": "Step 6: To serve: Spread base of buns with sauce / condiment of choice. Top with lettuce then tomato, then hamburger patty. Pile over onions, sliced pickles, then more sauce/condiments. Top with lid of bun. Serve immediately.", "underline": ["sliced"], "gif": "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzRkeHNnaXlsNnczb3EzYWl4dWl2Zzd1N2t0eGY0ZGE1c2t6dWlnZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iFyhAdgFB8kuzDN9gY/giphy.gif"},
        
    ]
    return render_template("index.html", steps = steps)

@auth.route('/ingredients')
def ingredients():
    ingredients = {
    "kg beef mince": 1,   # in grams
    "burger buns": 4, 
    "olive oil": 2,  # in grams
    "slices burger cheese": 8,   # in grams
    "lettuce leaves": 8,      # count
    "tomatoes": 2,
    "onions": 3,
       # in ml
}
    servings = request.args.get('servings', 4, type=int)
    selected_ingredient = request.args.get('selected_ingredient', None)
    factor = servings / 4

    adjusted_ingredients = {ingredient: round(amount * factor, 2) for ingredient, amount in ingredients.items()}

    substitutes = []
    if selected_ingredient:
        url = f'https://api.spoonacular.com/food/ingredients/substitutes?ingredientName={selected_ingredient}&apiKey={SPOONACULAR_API_KEY}'
        response = requests.get(url)
        data = response.json()

        if 'status' in data and data['status'] == 'success' and 'substitutes' in data:
            substitutes = data['substitutes']
        elif 'message' in data:
            substitutes = [data['message']]  # Handle specific error message from API
        else:
            substitutes = ["No substitutes found"]

    return render_template("ingredients.html", ingredients=ingredients, adjusted_ingredients=adjusted_ingredients, servings=servings, substitutes=substitutes, selected_ingredient=selected_ingredient)

# @auth.route('/substitutes/<ingredient>')
# def get_substitutes(ingredient):
#     url = f'https://api.spoonacular.com/food/ingredients/substitutes?ingredientName={ingredient}&apiKey={SPOONACULAR_API_KEY}'
#     response = requests.get(url)
#     data = response.json()
    
#     if 'substitutes' in data:
#         substitutes = data['substitutes']
#     else:
#         substitutes = ["No substitutes found"]
    
#     return jsonify(substitutes=substitutes)