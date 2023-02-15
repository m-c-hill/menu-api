# Restaurant Menu API

Menu REST API built using Flask, allowing customers to browse a list of dishes, filter them by category and place orders.

## Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses for our REST API.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are the ORM (Object-relatonal mapping) libraries of choice, used to define our domain models and handle all database interactions.

- [Alembic](https://alembic.sqlalchemy.org/en/latest/) and [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) are lightweight database migration tools used to manage changes to the domain models and update the database accordingly.

- [Pytest](https://docs.pytest.org/en/7.1.x/contents.html) was used as the testing framework for this project.

## Start the API

Run `docker compose up -d` and access the server through [localhost:5000/api/v1.0](http://127.0.0.1:5000/api/v1.0/).

### Testing

All tests can be found in the `test` directory. To run the tests, simply run:

```bash
python -m pytest
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

README IN PROGRESS

