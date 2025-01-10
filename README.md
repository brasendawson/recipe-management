Recipe Management API
Overview
The Recipe Management API allows users to create, update, delete, and search for recipes. It also supports searching recipes by ingredients and filtering them by categories.

Key Features:
List all recipes.
Create new recipes (requires authentication).
Retrieve, update, or delete specific recipes.
Search recipes by ingredients.
Filter recipes by category.
Technologies
Django
Django REST Framework
SQLite (or other databases)
Python 3.x
Setup Instructions
Prerequisites
Ensure that you have the following installed:

Python 3.x: Install from Python Official Website
pip: Python's package manager (usually bundled with Python installation)
virtualenv: Recommended to use for creating a virtual environment
1. Clone the repository
Clone the repository to your local machine:



git clone https://github.com/brasendawson/recipe-management.git
cd recipe-management
2. Set up a Virtual Environment
Create and activate a virtual environment:

On Windows:


python -m venv venv
venv\Scripts\activate
On Mac/Linux:


python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install the required dependencies from requirements.txt:


pip install -r requirements.txt
4. Apply Migrations
Run the migrations to set up the database schema:



python manage.py migrate
5. Create a Superuser (Optional)
If you want to access the Django admin interface, you can create a superuser:



python manage.py createsuperuser
Follow the prompts to create your superuser account.

6. Run the Development Server
Start the Django development server:


python manage.py runserver
The API will be accessible at http://127.0.0.1:8000/.

API Endpoints
1. List and Create Recipes
GET: /api/recipes/ - Retrieve a list of all recipes.
POST: /api/recipes/ - Create a new recipe (requires authentication).
2. Retrieve, Update, and Delete a Recipe
GET: /api/recipes/{id}/ - Retrieve a specific recipe by ID.
PUT: /api/recipes/{id}/ - Update an existing recipe (requires authentication).
DELETE: /api/recipes/{id}/ - Delete a recipe (requires authentication).
3. Search Recipes by Ingredient
GET: /api/recipes/ingredient/{ingredient}/ - Search recipes by ingredient.
4. Search Recipes
GET: /api/recipes/?search={query} - Search recipes by a keyword in the title or description.
5. Filter Recipes by Category
GET: /api/recipes/?category={category} - Filter recipes by category.
Authentication
The API supports token-based authentication. You can obtain a token using the obtain_auth_token endpoint from Django REST Framework's authtoken app.
Include the token in the Authorization header of each request:


Authorization: Bearer <your_token>
Testing the API
You can test the API endpoints using tools like Postman or cURL.

Example:

To create a new recipe:


curl -X POST http://127.0.0.1:8000/api/recipes/ \
    -H "Authorization: Bearer <your_token>" \
    -d '{"title": "Spaghetti Bolognese", "description": "A classic Italian pasta dish.", "ingredients": "spaghetti, ground beef, tomato sauce, onions, garlic", "instructions": "Cook spaghetti and brown the beef.", "category": "Main Course", "prep_time": 10, "cook_time": 30, "servings": 4}'
