### Applying Migrations
Migrations are essential to transit the DB into the working state. 

**First, ensure that you have a postgres DB called "delivery_service_db" created and running.**

Then, execute default Django commands:

`python src/manage.py makemigrations delivery_service`

`python src/manage.py migrate`