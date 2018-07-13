import psycopg2
from config import config
#!/usr/bin/python
def delete_part(rut):
    """ eliminar cliente por rut """
    conn = None
    rows_deleted = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("DELETE FROM clientes WHERE cliente_rut = %s", (rut,))
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted
#if __name__ == '__main__':
    #deleted_rows = delete_part(2)
    #print('The number of deleted rows: ', deleted_rows)
