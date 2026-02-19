import psycopg2

db_config = {
    "host": "localhost",
    "dbname": "web_scrap_project",
    "user": "postgres",
    "password": "Hellopsql",
    "port": "5432",
}


def get_connection():
    try:
        conn = psycopg2.connect(**db_config)
        return conn
    except psycopg2.OperationalError as e:
        print(f"WARNING: Can not connect to database. {e}")
        return None


def create_table():
    conn = get_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products(
                id SERIAL PRIMARY KEY,
                name VARCHAR(255),
                description TEXT,
                price DECIMAL(10,2),
                scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """
        )

        conn.commit()
        print("SUCCESS: product table created or already exits")
    except Exception as e:
        print(f"WARNING: can't create table: {e}")
    finally:
        cursor.close()
        conn.close()


def save_to_database(products):
    if not products:
        print("no products to save.")
        return

    conn = get_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        for product in products:
            cursor.execute(
                """
            INSERT INTO products (name, description, price) VALUES (%s, %s, %s);
            """,
                (product["name"], product["description"], product["price"]),
            )
        conn.commit()
        print(f"SUCCESS: {len(products)} products saved to database.")

    except Exception as e:
        conn.rollback()
        print(f"WARNING: can not save to db: {e}")
    finally:
        cursor.close()
        conn.close()

def fetch_from_database():
    conn = get_connection()
    if conn is None:
        return []
    
    try:
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT id, name, description, price, scraped_at FROM products;
        """)
        rows = cursor.fetchall() # rows is list of each row(tuple)
        
        # converting tuples into dictionary
        products = []
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "description": row[2],
                "price": float(row[3]),
                "scraped_at": str(row[4])
            })
        print(f"SUCCESS: fetched {len(products)} from database")
        return products
    except Exception as e:
        print(f"ERROR: can not fetch from the database")
        return []
    finally:
        cursor.close()
        conn.close()
create_table()