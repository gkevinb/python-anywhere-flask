# Flask app on pythonanywhere.com

Link: https://gkevinb.pythonanywhere.com/


## Docker

Need to also rebuild docker to see code changes, then start it up
```
docker-compose build && docker-compose up
```

To shut it down, CTRL + c but also run following to make sure it stopped
```
docker-compose down
```

In the database docker container, the `container_name` corresponds to the `hostname` in the SQL connector in the code. While the `hostname` in the docker container corresponds to the `host` in the server status page in MySQL Workbench.

https://stackoverflow.com/questions/57642582/mysql-connector-errors-databaseerror-2003-hy000-cant-connect-to-mysql-serve

## Pythonanywhere

https://www.pythonanywhere.com/batteries_included/

Don't use custom virtual envs, if you want to use the packages in [batteries_included](https://www.pythonanywhere.com/batteries_included/).


### Virtualenvs

Virutal environment (venv) found in `server/venv/`

Activate and deactivate venv

```bash
source server/venv/bin/activate
deactivate
```

Install packages from `requirements.txt` into venv. Make sure venv is active.

```bash
pip install -r server/src/requirements.txt
```

https://help.pythonanywhere.com/pages/RebuildingVirtualenvs/

## Vue JS Integration

https://dev.to/michaelbukachi/flask-vue-js-integration-tutorial-2g90

https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/

## Flask Best Practices

https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/

https://flask.palletsprojects.com/en/1.1.x/blueprints/#blueprints

## SQL and Databases

To run SQL commands go to the Databases tab and start a console on the database you want to edit. Then you can run any SQL queries you create locally on SQL Workbench, just copy and paste the exact commands and it runs exactly the same.

Look into way of running not just individual commands but entire scripts after getting better at SQL.


https://peewee.readthedocs.io/en/latest/index.html

https://hackersandslackers.com/python-database-management-sqlalchemy/

https://leportella.com/sqlalchemy-tutorial.html

https://blog.pythonanywhere.com/121/

https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure


## Testing

https://medium.com/swlh/automate-python-testing-with-github-actions-7926b5d8a865

## CSS

https://pythonhow.com/add-css-to-flask-website/