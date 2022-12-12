import pymysql
from config import host, user, password, db_name

TABLES_TITLES = ["users", "place", "user_place", "menu", "event", "promotion", "count_reviews"]

con = pymysql.connect(
    host=host,
    port=3306,
    user=user,
    password=password,
    cursorclass=pymysql.cursors.DictCursor
)

"""

DELIMITER //
CREATE PROCEDURE project_db.proc_1 (a int, b char(20))
BEGIN
    select * 
    from project_db.menu
    where place_id = a and title = b;
END //
DELIMITER ;

call project_db.proc_1(1, "Coffee 1");

"""

"""

delimiter $$
create function project_db.price_coef(kk float, price float) returns int
deterministic
begin
	DECLARE c float;
	SET c = price * kk;
	return c;
END;
$$
delimiter ;

"""


def sql_procedure_menu(place_id, menu_title):
    request = f"CALL project_db.proc_1({place_id}, '{menu_title}');"
    with con.cursor() as cur:
        cur.execute(request)
        return cur.fetchall()[0]


# print(sql_procedure_menu(14, "Coffee 3"))


def sql_function_menu_price(value, coef=0.9):
    request = f"SELECT project_db.price_coef({value}, {coef});"
    with con.cursor() as cur:
        cur.execute(request)
        return cur.fetchone()[f'project_db.price_coef({value}, {coef})']


# print(str(sql_function_menu_price(100)))


def create_main_db():
    try:
        request = f"CREATE DATABASE IF NOT EXISTS project_db;"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_users_table():
    try:
        request = "CREATE TABLE IF NOT EXISTS project_db.users (id int AUTO_INCREMENT," \
                  "name VARCHAR(50) UNIQUE," \
                  "PRIMARY KEY(id));"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_place_table():
    try:
        request = "CREATE TABLE IF NOT EXISTS project_db.place (id int AUTO_INCREMENT, " \
                  "type VARCHAR(100)," \
                  "title VARCHAR(100) UNIQUE," \
                  "description VARCHAR(200)," \
                  "PRIMARY KEY(id));"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_user_place_table():
    try:
        request = "CREATE TABLE IF NOT EXISTS project_db.user_place (place_id INT," \
                  "user_id INT," \
                  "review VARCHAR(200)," \
                  "FOREIGN KEY(place_id) REFERENCES place(id) ON DELETE CASCADE ON UPDATE CASCADE," \
                  "FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE," \
                  "PRIMARY KEY(place_id, user_id));"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_menu_table():
    # try:
    request = "CREATE TABLE IF NOT EXISTS project_db.menu (title VARCHAR(100)," \
              "description VARCHAR(500)," \
              "place_id INT," \
              "price FLOAT," \
              "FOREIGN KEY(place_id) REFERENCES place(id) ON DELETE CASCADE ON UPDATE CASCADE," \
              "PRIMARY KEY(place_id, title));"
    with con.cursor() as cur:
        cur.execute(request)
        con.commit()
        return True
    # except Exception:
    #     return False


def create_event_table():
    try:
        request = "CREATE TABLE IF NOT EXISTS project_db.event (place_id INT," \
                  "title VARCHAR(100)," \
                  "description VARCHAR(500)," \
                  "FOREIGN KEY(place_id) REFERENCES place(id) ON DELETE CASCADE ON UPDATE CASCADE," \
                  "PRIMARY KEY(place_id, title));"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_promotion_table():
    try:
        request = "CREATE TABLE IF NOT EXISTS project_db.promotion (place_id INT," \
                  "title VARCHAR(100)," \
                  "description VARCHAR(500)," \
                  "FOREIGN KEY(place_id) REFERENCES place(id) ON DELETE CASCADE ON UPDATE CASCADE," \
                  "PRIMARY KEY(place_id, title));"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def create_count_reviews_table():
    try:
        request = "CREATE TABLE IF NOT EXISTS project_db.count_reviews (place_id INT," \
                  "count INT," \
                  "FOREIGN KEY(place_id) REFERENCES place(id) ON DELETE CASCADE ON UPDATE CASCADE," \
                  "PRIMARY KEY(place_id));"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


print("*" * 100)
print(create_main_db())
print(create_users_table())
print(create_place_table())
print(create_user_place_table())
print(create_menu_table())
print(create_event_table())
print(create_promotion_table())
print(create_count_reviews_table())
print("*" * 100)


def describe_users_table():
    show_table_query = "DESCRIBE project_db.users"
    with con.cursor() as cur:
        cur.execute(show_table_query)
        # Fetch rows from last executed query
        result = cur.fetchall()
        for row in result:
            print(row)


def describe_place_table():
    show_table_query = "DESCRIBE project_db.place"
    with con.cursor() as cur:
        cur.execute(show_table_query)
        # Fetch rows from last executed query
        result = cur.fetchall()
        for row in result:
            print(row)


def describe_user_place_table():
    show_table_query = "DESCRIBE project_db.user_place"
    with con.cursor() as cur:
        cur.execute(show_table_query)
        # Fetch rows from last executed query
        result = cur.fetchall()
        for row in result:
            print(row)


def describe_menu_table():
    show_table_query = "DESCRIBE project_db.menu"
    with con.cursor() as cur:
        cur.execute(show_table_query)
        # Fetch rows from last executed query
        result = cur.fetchall()
        for row in result:
            print(row)


def describe_event_table():
    show_table_query = "DESCRIBE project_db.event"
    with con.cursor() as cur:
        cur.execute(show_table_query)
        # Fetch rows from last executed query
        result = cur.fetchall()
        for row in result:
            print(row)


def describe_promotion_table():
    show_table_query = "DESCRIBE project_db.promotion"
    with con.cursor() as cur:
        cur.execute(show_table_query)
        # Fetch rows from last executed query
        result = cur.fetchall()
        for row in result:
            print(row)


def describe_count_reviews_table():
    show_table_query = "DESCRIBE project_db.count_reviews"
    with con.cursor() as cur:
        cur.execute(show_table_query)
        # Fetch rows from last executed query
        result = cur.fetchall()
        for row in result:
            print(row)


# describe_users_table()
# print()
# describe_place_table()
# print()
# describe_user_place_table()
# print()
# describe_menu_table()
# print()
# describe_event_table()
# print()
# describe_promotion_table()
# print()
# describe_count_reviews_table()
# print()


def add_user_in_table(user_name):
    try:
        request = "INSERT INTO project_db.users (name) VALUES (%s)"
        record = [(user_name,)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
        return True
    except Exception:
        return False


def add_place_in_table(place_type, title, description):
    try:
        request = "INSERT INTO project_db.place (type, title, description) VALUES (%s, %s, %s)"
        record = [(place_type, title, description)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()

            request = "SELECT id FROM project_db.place WHERE title = (%s)"
            cur.execute(request, (title))
            place_id = cur.fetchall()[0]["id"]
            add_count_reviews_in_table(place_id)

        return True
    except Exception:
        return False


def add_user_place_in_table(place_id, user_id, review):
    try:
        request = "INSERT INTO project_db.user_place (place_id, user_id, review) VALUES (%s, %s, %s)"
        record = [(place_id, user_id, review)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
        return True
    except Exception:
        return False


def add_menu_in_table(title, description, place_id, price):
    try:
        request = "INSERT INTO project_db.menu (title, description, place_id, price) VALUES (%s, %s, %s, %s)"
        record = [(title, description, place_id, price)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
        return True
    except Exception:
        return False


def add_event_in_table(place_id, title, description):
    try:
        request = "INSERT INTO project_db.event (place_id, title, description) VALUES (%s, %s, %s)"
        record = [(place_id, title, description)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
        return True
    except Exception:
        return False


def add_promotion_in_table(place_id, title, description):
    try:
        request = "INSERT INTO project_db.promotion (place_id, title, description) VALUES (%s, %s, %s)"
        record = [(place_id, title, description)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
        return True
    except Exception:
        return False


def add_count_reviews_in_table(place_id):
    try:
        request = "INSERT INTO project_db.count_reviews (place_id, count) VALUES (%s, %s)"
        record = [(place_id, 0)]
        with con.cursor() as cur:
            cur.executemany(request, record)
            con.commit()
        return True
    except Exception:
        return False


place_index = 4
print("#" * 100)
print(add_user_in_table("Bill"))
print(add_place_in_table("Усадьба", "Дом Дурасовых", "Такое описание"))
print(add_user_place_in_table(place_index, 1, "Хорошо"))
print(add_menu_in_table("Coffee 3", "Taste coffee", place_index, 450))
print(add_event_in_table(place_index, "New Year Party", "Big party before the New Year"))
print(add_promotion_in_table(place_index, "discount", "big discount of all"))
print("*" * 100)


def show_table(table_title):
    if table_title in TABLES_TITLES:
        request = f"SELECT * FROM project_db.{table_title}"
        with con.cursor() as cur:
            cur.execute(request)
        return cur.fetchall()


def get_place_title(title):
    request = f"SELECT * FROM project_db.place WHERE title = {title};"
    with con.cursor() as cur:
        cur.execute(request)
    return cur.fetchall()[0]


print("*" * 100)
print(show_table("users"))
print(show_table("place"))
print(show_table("event"))
print(show_table("promotion"))
print(show_table("menu"))
print(show_table("user_place"))
print(show_table("count_reviews"))
print("*" * 100)


def del_user_in_table(name):
    try:
        request = f"DELETE FROM project_db.users WHERE name = '{name}'"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def del_place_in_table(title):
    # try:
    request = f"DELETE FROM project_db.place WHERE title = '{title}'"
    with con.cursor() as cur:
        cur.execute(request)
        con.commit()
        return True
    # except Exception:
    #     return False


# print(del_place_in_table("Хачапури и вино"))


def del_user_place_in_table(place_id, user_id):
    # try:
    request = f"DELETE FROM project_db.user_place WHERE place_id = '{place_id}' and user_id = '{user_id}'"
    with con.cursor() as cur:
        cur.execute(request)
        con.commit()
        return True
    # except Exception:
    #     return False


def del_menu_in_table(place_id, title):
    # try:
    request = f"DELETE FROM project_db.menu WHERE place_id = '{place_id}' and title = '{title}'"
    with con.cursor() as cur:
        cur.execute(request)
        con.commit()
        return True
    # except Exception:
    #     return False


def del_event_in_table(place_id, title):
    try:
        request = f"DELETE FROM project_db.event WHERE place_id = '{place_id}' and title = '{title}'"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


def del_promotion_in_table(place_id, title):
    try:
        request = f"DELETE FROM project_db.promotion WHERE place_id = '{place_id}' and title = '{title}'"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
            return True
    except Exception:
        return False


print("#" * 100)
# print(del_event_in_table(1, "New Year Party"))
# print(del_promotion_in_table(1, "discount"))
# print(del_menu_in_table(3, "Coffee 1"))
# print(del_user_place_in_table(11, 34))


"""

-- CREATE TRIGGER project_db.up_count_reviews AFTER INSERT ON project_db.user_place
-- FOR EACH ROW UPDATE project_db.count_reviews SET count = (count + 1) WHERE place_id = NEW.place_id;

"""

"""

-- CREATE TRIGGER project_db.down_count_reviews BEFORE DELETE ON project_db.user_place
-- FOR EACH ROW UPDATE project_db.count_reviews SET count = (count - 1) WHERE place_id = OLD.place_id;

"""


def create_trigger_up_count_reviews():
    request = """

-- CREATE TRIGGER project_db.down_count_reviews BEFORE DELETE ON project_db.user_place
-- FOR EACH ROW UPDATE project_db.count_reviews SET count = (count - 1) WHERE place_id = OLD.place_id;

"""
    with con.cursor() as cur:
        cur.execute(request)
        con.commit()
        return True


def create_trigger_down_count_reviews():
    request = """

-- CREATE TRIGGER project_db.down_count_reviews BEFORE DELETE ON project_db.user_place
-- FOR EACH ROW UPDATE project_db.count_reviews SET count = (count - 1) WHERE place_id = OLD.place_id;

"""
    with con.cursor() as cur:
        cur.execute(request)
        con.commit()
        return True


# print("#"*100)
# print(create_trigger_up_count_reviews())
# print(create_trigger_down_count_reviews())


def drop_user_table():
    try:
        request = "DROP TABLE users;"
        with con.cursor() as cur:
            cur.execute(request)
            con.commit()
        return True
    except Exception:
        return False

# print(drop_user_table())
# with con.cursor() as cur:
#     create_table_query = "CREATE TABLE IF NOT EXISTS test_two (id int AUTO_INCREMENT," \
#                          "name varchar(32)," \
#                          "password varchar(32)," \
#                          "PRIMARY KEY (id));"
#     cur.execute(request_create_all_table)


# with con.cursor() as cur:
#     add_query = "INSERT INTO test_one (name, password) VALUES ('anna', 'qwerty');"
#     cur.execute(add_query)
#     con.commit()


# with con.cursor() as cur:
#     # query = "SELECT * FROM users"
#     cur.execute("SELECT * FROM test_one")
#     print(cur.fetchall())
