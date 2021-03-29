import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """
    create a database connection to the SQLite database specified by db_file
    var db_file: database file
    return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_user(conn, user):
    """
    Uses Connection object and some data (?, ?, ?) to write a row into table:
      table_1
    """
    sql = ''' INSERT INTO user(user_id, username, first_name, last_name, email, password_hash, is_admin, module_1, module_2, module_3)
              VALUES(?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()


def create_multiple(conn, multiple):
    """
    Uses connection object and some data (?, ?, ?, ?) to write a row into table:
      table_2
    """
    sql = ''' INSERT INTO multiple(question_id, question, correct, incorrect_1, incorrect_2, incorrect_3, module_code, date_created, difficulty, is_formative, feedback)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, multiple)
    conn.commit()

def create_assessment(conn, assessment):
    """
    Uses connection object and some data (?, ?, ?, ?) to write a row into table:
      table_2
    """
    sql = ''' INSERT INTO multiple(assessment_id, assessment_name, module_code, admin_created, q1_type, q1_id, q2_type, q2_id, q3_type, q3_id)
              VALUES(?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, assessment)
    conn.commit()

def create_fill(conn, fill):
    """
    Uses connection object and some data (?, ?, ?, ?) to write a row into table:
      table_2
    """
    sql = ''' INSERT INTO multiple(question_id, question, correct, blank_1, blank_2, blank_3, module_code, date_created, difficulty, is_formative, feedback)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, fill)
    conn.commit()

def create_attempts(conn, attempts):
    """
    Uses connection object and some data (?, ?, ?, ?) to write a row into table:
      table_2
    """
    sql = ''' INSERT INTO multiple(attempt_id, user_id, assessment_id, attempt_no, answer_1, correct_1, answer_2, correct_2, answer_3, correct_3, ratio_correct, module_code, datetime_created, is_formative)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, attempts)
    conn.commit()

def main():
    database = r"aat_v1.db"

    # create a database connection
    conn = create_connection(database)
    with conn:


        '''
        CREATE USER (user)

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
        '''

        user1 = (1, "Admin", "The", "Boss", "thequizmaster@university.com", "", True, "CMT001", "CMT002", "CMT003")


        '''
        CREATE MULTIPLE (multiple)

        question_id integer PRIMARY KEY,
        question text NOT NULL,
        correct text NOT NULL,
        incorrect_1 text NOT NULL.
        incorrect_2 text NOT NULL,
        incorrect_3 text NOT NULL,
        module_code text NOT NULL,
        date_created date NOT NULL,
        difficulty text NOT NULL,
        is_formative boolean NOT NULL,
        feedback text NOT NULL
        '''

        multiple1 = (1, "What colour are bananas?", "yellow", "blue", "red", "purple", "CMT001", "YYYY-MM-DD", "easy", False, "Incorrect, check out the lecture on fruit for a hint")



        # put the people vars created above into the table:  table_1
        create_user(conn, user1)


        # put the animal vars created above into the table:  table_2
        create_multiple(conn, multiple1)


        # print tables to terminal to see -
        def print_table(conn, table_name):
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM {table_name}")
            print(cur.fetchall())

        print_table(conn, "user")

        print_table(conn, "multiple")


# run the script - will populate 'var database' in the same directory.
# (the database will contain data defined here)
# https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':
    main()


#  The created table can be viewed easily at:  https://inloop.github.io/sqlite-viewer/
#    You can simply drag-and-drop the .db file into this page.
