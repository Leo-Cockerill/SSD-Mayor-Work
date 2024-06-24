from flask import Blueprint, render_template, request, flash, jsonify
import requests


auth = Blueprint('auth', __name__)


SPOONACULAR_API_KEY = '2fd8fa8f5091434a9701a9ab5c92d235'

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
    return render_template("steps.html", steps = steps)

@auth.route('/ingredients')
def ingredients():
    ingredients = {
    "kg beef mince": 1,   # in grams
    "burger buns": 4, 
    "olive oil": 2,  # in grams
    "cheese slices": 8,   # in grams
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


@auth.route('/cooking-skills')  
def cooking_skills():
    return render_template("cooking-skills.html")

@auth.route('/ingredient-info', methods=['GET'])
def ingredient_info():
    ingredient_name = request.args.get('ingredient')
    if not ingredient_name:
        return jsonify({"error": "No ingredient provided"}), 400

    search_url = f'https://api.spoonacular.com/food/ingredients/search?query={ingredient_name}&apiKey={SPOONACULAR_API_KEY}'
    search_response = requests.get(search_url)

    if search_response.status_code != 200:
        return jsonify({"error": "Error fetching ingredient information"}), 500

    search_data = search_response.json()
    if not search_data['results']:
        return jsonify({"error": "Ingredient not found"}), 404

    ingredient_id = search_data['results'][0]['id']

    info_url = f'https://api.spoonacular.com/food/ingredients/{ingredient_id}/information?amount=1&apiKey={SPOONACULAR_API_KEY}'
    info_response = requests.get(info_url)

    if info_response.status_code != 200:
        return jsonify({"error": "Error fetching detailed ingredient information"}), 500

    ingredient_info = info_response.json()

    # Exchange rate for USD to AUD (you may want to fetch this dynamically)
    usd_to_aud_rate = 1.45

    # Converting cost to AUD and dividing by 100
    if 'estimatedCost' in ingredient_info and ingredient_info['estimatedCost']:
        ingredient_info['estimatedCost']['value'] = (ingredient_info['estimatedCost']['value'] * usd_to_aud_rate) / 100
        ingredient_info['estimatedCost']['unit'] = 'AUD'

    # Nutrition information we want to display
    nutrition_info = ingredient_info.get('nutrition', {}).get('nutrients', [])
    required_nutrients = [
        'Calories', 'Carbohydrates', 'Protein', 'Fat', 'Saturated Fat', 'Polyunsaturated Fat', 
        'Monounsaturated Fat', 'Trans Fat', 'Cholesterol', 'Sodium', 'Potassium', 'Fiber', 
        'Sugar', 'Vitamin A', 'Vitamin C', 'Calcium', 'Iron'
    ]
    formatted_nutrition = {nutrient['name']: f"{nutrient['amount']} {nutrient['unit']} ({nutrient.get('percentOfDailyNeeds', '')}%)" 
                           for nutrient in nutrition_info if nutrient['name'] in required_nutrients}

    ingredient_info['formatted_nutrition'] = formatted_nutrition
    return jsonify(ingredient_info)


