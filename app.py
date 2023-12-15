from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Sample data - replace with actual data
# restaurants = [
#     {'name': 'Restaurant A', 'cuisine': 'Italian', 'rating': 4.5, 'price': '$$', 'url': 'https://www.yelp.com/biz/restaurant-a', 'distance': 400},
#     {'name': 'Restaurant B', 'cuisine': 'Chinese', 'rating': 4.1, 'price': '$', 'url': 'https://www.yelp.com/biz/restaurant-b', 'distance': 550},
#     {'name': 'Restaurant C', 'cuisine': 'Japanese', 'rating': 4.0, 'price': '$$$', 'url': 'https://www.yelp.com/biz/restaurant-c', 'distance': 750},
#     {'name': 'Restaurant D', 'cuisine': 'Korean', 'rating': 4.9, 'price': '$', 'url': 'https://www.yelp.com/biz/restaurant-d', 'distance': 1390},
#     {'name': 'Restaurant E', 'cuisine': 'Mexican', 'rating': 4.7, 'price': '$$', 'url': 'https://www.yelp.com/biz/restaurant-e', 'distance': 1280}
#     # ... more restaurants
# ]

with open('F:\\tree\\Umich New Life\\study related\\2023 Fall\\SI 507\\Final project\\restaurants.json', 'r') as file:
    restaurants = json.load(file)

# Handle NaN values in 'price'
# restaurants = [{**r, 'price': r['price'] if 'price' in r and r['price'] is not None else 'Unknown'} for r in restaurants]

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_cuisine = request.form.get('main_category')
    selected_price = request.form.get('price')
    selected_rating = request.form.get('rating')
    selected_distance = request.form.get('distance')

    # Initialize filtered_restaurants with all restaurants
    filtered_restaurants = restaurants

    # Filter restaurants based on rating range
    if selected_rating == "4.5":
        filtered_restaurants = [r for r in restaurants if r['rating'] >= 4.5]
    elif selected_rating == "4.0":
        filtered_restaurants = [r for r in restaurants if 4.0 <= r['rating'] < 4.5]
    elif selected_rating == "0":
        filtered_restaurants = [r for r in restaurants if r['rating'] < 4.0]
    
    # Apply cuisine filter
    if selected_cuisine and selected_cuisine != '':
        filtered_restaurants = [r for r in filtered_restaurants if r['main_category'] == selected_cuisine]

    # Apply price filter
    if selected_price and selected_price != '':
        filtered_restaurants = [r for r in filtered_restaurants if r['price'] == selected_price]   
    
    # Apply distance filter
    if selected_distance:
        if selected_distance == "500":
            filtered_restaurants = [r for r in filtered_restaurants if r['distance'] < 500]
        elif selected_distance == "1500":
            filtered_restaurants = [r for r in filtered_restaurants if 500 <= r['distance'] <= 1500]
        elif selected_distance == "1501":
            filtered_restaurants = [r for r in filtered_restaurants if r['distance'] > 1500]


    # Extract unique cuisines and prices for dropdowns
    cuisines = sorted(set(r['main_category'] for r in restaurants))
    prices = sorted(set(r['price'] for r in restaurants))

    return render_template('template.html',
                           cuisines=cuisines,
                           prices=prices,
                           restaurants=filtered_restaurants)

if __name__ == '__main__':
    app.run(debug=True)