### Prerequisites

1. Virtual environment and installed requirements.
2. Applied migrations.


### Running tests

To run unit tests only, execute:

`python src/manage.py test tests/unit`

To run integration tests only, execute:

`python src/manage.py test tests/integration`

To run all tests, execute:

`python src/manage.py test tests`

#### Note:
The tests do not require the programmer to manually create the database and populate it with data. 
Django framework creates the database and applies migrations under the hood. 
Also, the tests use fixtures that load all necessary data into the DB. 