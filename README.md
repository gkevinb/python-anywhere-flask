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

https://help.pythonanywhere.com/pages/RebuildingVirtualenvs/

## SQL and Databases

To run SQL commands go to the Databases tab and start a console on the database you want to edit. Then you can run any SQL queries you create locally on SQL Workbench, just copy and paste the exact commands and it runs exactly the same.

Look into way of running not just individual commands but entire scripts after getting better at SQL.


https://peewee.readthedocs.io/en/latest/index.html

https://hackersandslackers.com/python-database-management-sqlalchemy/

https://leportella.com/sqlalchemy-tutorial.html

https://blog.pythonanywhere.com/121/

https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/

https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/