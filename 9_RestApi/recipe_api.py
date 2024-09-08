from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for the API
recipes = {
    1: {'id': 1, 'title': 'Spaghetti Carbonara', 'ingredients': ['spaghetti', 'eggs', 'pecorino cheese', 'guanciale'],
        'instructions': 'Cook pasta, fry guanciale, mix with eggs and cheese, and combine with pasta.'},
    2: {'id': 2, 'title': 'Tomato Soup', 'ingredients': ['tomato', 'water', 'salt'],
        'instructions': 'Boil all together until mushy, blend, and serve.'},
    3: {'id': 3, 'title': 'Grilled Cheese Sandwich', 'ingredients': ['bread', 'cheese', 'butter'],
        'instructions': 'Butter bread, place cheese between slices, grill until golden.'}
}


# Route to get all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify(list(recipes.values()))


# Route to get a specific recipe by ID
@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = recipes.get(recipe_id)
    if recipe:
        return jsonify(recipe)
    return jsonify({'message': 'Recipe not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
