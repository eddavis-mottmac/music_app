import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# DONE IMPLEMENT DATABASE URL
# I've used MSSQL database as I can't get approval at work to use the Postgres SQL db.
# The URI string for Postgre should replace the string below in the following format: 'postgresql://username:password@host:port/database_name'
SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://@(localdb)\MSSQLLocalDB/Fyyur?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'