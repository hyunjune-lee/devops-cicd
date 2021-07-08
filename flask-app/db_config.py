from app import app
from flaskext.mysql import MySQL
import os

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "mysecret"
app.config["MYSQL_DATABASE"] = "daily_quiz"
app.config["MYSQL_DATABASE_HOST"] = "localhost"

mysql.init_app(app)
