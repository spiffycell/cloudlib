"""Postgres object."""

# standard imports
import logging
import os
import psycopg2

# env vars
POSTGRES_USER = os.getenv("POSTGRES_USER", None)
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", None)
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "127.0.0.1")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", 5432)
POSTGRES_DB = os.getenv("POSTGRES_DB", "test")

class Postgres:
    """ Simple Postgres object."""
    def __init__(self):
        """
        Init Postgres object. 
        We pass in a db_config object, which has the form:
        ```
        db_config = {
            user="",
            password="",
            host="",
            port="",
            database=""
        }
        ```
        """
        # connect to a database
        try:
            logging.info("Connecting to db %s on %s:%s", \
                    db_config["database"], \
                    db_config["host"], \
                    db_config["port"] \
                    )
            self.conn = psycopg2.connect(user=POSTGRES_USER, \
                    password=POSTGRES_PASSWORD, \
                    host=POSTGRES_HOST, \
                    port=POSTGRES_PORT, \
                    database=POSTGRES_DB \
                    )
            # set cursor on the database
            self.cur = self.conn.cursor()
            logging.info("Connection successful!")
        except psycopg2.OperationalError as exc:
            logging.error("Unable to connect to database: %s", exc)

    def exec(self, sql):
        """ Exec SQL query."""
        # pass in an SQL query to the database
        # get more info on structure of this method
        self.cursor.execute(sql)
        # get the returning id of the SQL query 
        ret_data = self.cursor.fetchall()
        return ret_data

    def create_table(self, table_name, columns, primkey):
        """
        Create Table.
        https://www.tutorialspoint.com/postgresql/postgresql_create_table.htm

        Table configs per database will be specified in YAML files
        The handler for this method will parse the YAML and send the output \
                to this method in order to create the necessary tables.
        """
        # start the query
        sql = f"CREATE TABLE {table_name}("

        # add in each column
        for column in columns:
            sql += f"{column['name']} {column['dtype']},"
        
        # finish query with primkey
        sql += "PRIMARY KEY({primkey}))"

        # execute the query
        self.exec(sql)
        return table

    def update_table(self, table):
        """ Update Table."""
        sql = ""
        self.exec(sql)
        return table

    def delete_table(self, table):
        """ Delete Table."""
        sql = ""
        self.exec(sql)
        return table

    def create_user(self, user):
        """ Create User."""
        sql = ""
        self.exec(sql)
        return user

    def update_user(self, user):
        """ Update User."""
        sql = ""
        self.exec(sql)
        return user

    def delete_user(self, user):
        """ Delete User."""
        sql = ""
        self.exec(sql)
        return user

    def commit(self):
        """ Commit DB changes."""
        # permanently save changes to the db
        self.conn.commit()

    def close(self):
        """ Close DB Connection."""
        # close the cursor
        self.cursor.close()
        # close the connection
        self.conn.close()
