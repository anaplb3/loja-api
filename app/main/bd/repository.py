import app.main.bd.config as cfg
import psycopg2

def create_connection():
    return psycopg2.connect(
        host=cfg.POSTGRES_CFG['host'],
        port=cfg.POSTGRES_CFG['port'],
        dbname=cfg.POSTGRES_CFG['dbname'],
        user=cfg.POSTGRES_CFG['user'],
        password=cfg.POSTGRES_CFG['pwd']
    )


def init_bd():
    connection = create_connection()
    cursor = connection.cursor()

    create_table_items = """
        CREATE TABLE IF NOT EXISTS items(
            id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            price FLOAT NOT NULL,
            item_type VARCHAR NOT NULL,
            is_available BOOLEAN NOT NULL
        ) """
    create_table_clients = """

        CREATE TABLE IF NOT EXISTS clients(
            id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            cpf VARCHAR NOT NULL
        ) """

    create_table_operations = """
        CREATE TABLE IF NOT EXISTS operations(
            id SERIAL PRIMARY KEY,
            id_item INTEGER REFERENCES items(id),
            id_client INTEGER REFERENCES clients(id),
            operation_type VARCHAR NOT NULL,
            operation_date DATE NOT NULL
        ) """

    cursor.execute(create_table_items)
    cursor.execute(create_table_clients)
    cursor.execute(create_table_operations)
    
    connection.commit()
    connection.close()
