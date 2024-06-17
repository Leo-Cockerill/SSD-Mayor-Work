from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


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
    ingredients = ['Flour', 'Sugar', 'Eggs', 'Butter', 'Milk', 'Vanilla Extract', 'Baking Powder', 'Salt']
    return render_template("ingredients.html", ingredients=ingredients)

