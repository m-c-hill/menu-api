# Restaurant Menu API

Menu REST API built using Flask, allowing customers to browse a list of dishes, filter them by category and place orders.

### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses for our REST API.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are the ORM (Object-relatonal mapping) libraries of choice, used to define our domain models and handle all database interactions.

- [Alembic](https://alembic.sqlalchemy.org/en/latest/) and [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) are lightweight database migration tools used to manage changes to the domain models and update the database accordingly.

- [Pytest](https://docs.pytest.org/en/7.1.x/contents.html) was used as the testing framework for this project.

### Run the app

Run `docker compose up -d` and access the server through [localhost:5000/api/v1.0](http://127.0.0.1:5000/api/v1.0/).

Alternatively, the app can be run locally without a container using `flask run`, still accessed through port 5000.

### Run the tests

All tests can be found in the `test` directory. To run the tests, simply run:

```bash
./run-tests.sh
```

Example output:

```bash
platform linux -- Python 3.8.10, pytest-7.1.2, pluggy-1.0.0
rootdir: /home/matt/dev/boardgame-tracker
plugins: mock-3.8.2
collected 52 items

tests/test_dishes.py ........            [61%]
tests/test_index.py .                    [69%]
tests/test_orders.py ....                [100%]

============ 13 passed ============
```

### API Documentation

#### Dishes

`GET /dishes`: Retrieve a complete list of all dishes on the menu.

`GET /dishes/category/<string:category_name>`: Retrieve a list of dishes by category name. Categories include: `starters, mains, specials, sides, desserts, drinks`.

`GET /dishes/<int:dish_id>`: Retrieve a dish by id.

`POST /dishes`: Add a new dish to the menu by submitting data with the following structure:

```json
{
  "name": "Sushi",
  "description": "Fresh salmon in rice and nori",
  "price": 11.29,
  "hot_or_cold": "cold",
  "category": "mains",
  "ingredients": "Salmon, rice, nori"
}
```

`DELETE /dishes/<int:dish_id>`: Delete a dish by id.

#### Orders

`GET /orders/<int:order_id>`: Retrieve an order by id

`POST /orders`: Create a new order by submitting data with the following structure:

```json
{
  "customer_id": 1,
  "order_items": [
    { "dish_id": 1, "quantity": 2 },
    { "dish_id": 4, "quantity": 5 }
  ]
}
```

`PATCH /orders/<int:order_id>`: Cancel an order by id

### Example Requests

#### GET /dishes/4

Request:

```bash
curl http://127.0.0.1:5000/api/v1.0/dish/4
```

Response:

```json
{
  "dish": {
    "category": "desserts",
    "description": "Selection of chocolate and vanilla ice cream",
    "hot_or_cold": "cold",
    "id": 4,
    "ingredients": "Ice cream, wafer, chocolate sauce",
    "name": "Ice cream",
    "price": 5.99
  },
  "success": true
}
```

#### POST /dishes

Request:

```bash
curl http://127.0.0.1:5000/api/v1.0/dish -X POST -H "Content-Type: application/json" -d '{ "name": "Sushi", "description": "Fresh salmon in rice and nori", "price": 11.29, "hot_or_cold": "cold", "category": "mains", "ingredients": "Salmon, rice, nori"}'
```

Response:

```json
{
  "dish": {
    "category": "mains",
    "description": "Fresh salmon in rice and nori",
    "hot_or_cold": "cold",
    "id": 5,
    "ingredients": "Salmon, rice, nori",
    "name": "Sushi",
    "price": 11.29
  },
  "success": true
}
```

### Potential Improvements

- Database migration is not currently set up in the Docker container (tables are not created when running through a container). Should be a quick fix (with `manage.py`) but ran out of time. The app can also be run locally with `flask run`.
- Set up different user groups (customer, waiter, restaurant owner) and add authentication to endpoints to ensure customers cannot add items to the menu, and that customers cannot cancel orders that do not belong to them.
- Add Swagger documentation.
- Create a separate ingredients table to store ingredients, link to dishes by ID through an association table.
