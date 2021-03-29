import sqlite3
# What is SQLite -  https://www.sqlite.org/index.html
# SQLite in Python -  https://docs.python.org/3/library/sqlite3.html
# GeeksForGeeks Introduction Python, SQLite3 -  https://www.geeksforgeeks.org/introduction-to-sqlite-in-python/
from sqlite3 import Error


def create_connection(db_file):
    """
    create a database connection to the SQLite database specified by db_file
    var db_file: database file
    returns: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """
    create a table with the create_table_sql statement
    var conn: Connection object (from above, create_connection)
    var create_table_sql: a CREATE TABLE statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    # define database name
    database = r"aat_v1.db"

    # define table names and structure of tables (column names)
    sql_create_table_user = """ CREATE TABLE IF NOT EXISTS user (
                                user_id integer PRIMARY KEY,
                                username text NOT NULL,
                                first_name text NOT NULL,
                                last_name text NOT NULL,
                                email text NOT NULL,
                                password_hash text NOT NULL,
                                is_admin boolean NOT NULL,
                                module_1 text NOT NULL,
                                module_2 text NOT NULL,
                                module_3 text NOT NULL
                                ); """

    sql_create_table_multiple = """ CREATE TABLE IF NOT EXISTS multiple (
                                    question_id integer PRIMARY KEY,
                                    question text NOT NULL,
                                    correct text NOT NULL,
                                    incorrect_1 text NOT NULL,
                                    incorrect_2 text NOT NULL,
                                    incorrect_3 text NOT NULL,
                                    module_code text NOT NULL,
                                    date_created date NOT NULL,
                                    difficulty text NOT NULL,
                                    is_formative boolean NOT NULL,
                                    feedback text NOT NULL
                                    ); """

    sql_create_table_assessment = """ CREATE TABLE IF NOT EXISTS assessment (
                                    assessment_id integer PRIMARY KEY,
                                    assessment_name text NOT NULL,
                                    module_code integer NOT NULL,
                                    admin_created boolean NOT NULL,
                                    q1_type text NOT NULL,
                                    q1_id text NOT NULL,
                                    q2_type text NOT NULL,
                                    q2_id text NOT NULL,
                                    q3_type text NOT NULL,
                                    q3_id text NOT NULL
                                    ); """

    sql_create_table_fill = """ CREATE TABLE IF NOT EXISTS fill (
                                question_id integer PRIMARY KEY,
                                question text NOT NULL,
                                blank_1 text NOT NULL,
                                blank_2 text NOT NULL,
                                blank_3 text NOT NULL,
                                correct text NOT NULL,
                                module_code integer NOT NULL,
                                date_created date NOT NULL,
                                difficulty text NOT NULL,
                                is_formative boolean NOT NULL,
                                feedback text NOT NULL
                                ); """                                    

    sql_create_table_attempts = """ CREATE TABLE IF NOT EXISTS attempts (
                                    attempt_id integer PRIMARY KEY,
                                    user_id integer NOT NULL,
                                    assessment_id integer NOT NULL,
                                    attempt_no integer NOT NULL,
                                    answer_1 text NOT NULL,
                                    correct_1 boolean NOT NULL,
                                    answer_2 text NOT NULL,
                                    correct_2 boolean NOT NULL,
                                    answer_3 text NOT NULL,
                                    correct_3 boolean NOT NULL,
                                    ratio_correct float NOT NULL,
                                    module_code integer NOT NULL,
                                    datetime_created datetime NOT NULL,
                                    is_formative boolean NOT NULL
                                    ); """                                    

    # create a database connection
    conn = create_connection(database)

    # use variables established above to create tables as described
    if conn is not None:
        create_table(conn, sql_create_table_user)
        create_table(conn, sql_create_table_multiple)
        create_table(conn, sql_create_table_assessment)
        create_table(conn, sql_create_table_fill)
        create_table(conn, sql_create_table_attempts)
    else:
        print("Error! cannot create the database connection.")


# run the script - will produce 'var database' in the same directory.
# (the database will not contain any data)
# https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':
    main()
