#!/usr/bin/python

import psycopg2
from config import config
def iter_row(cursor):
    while True:
        rows = cursor.fetchmany()
        if not rows:
            break
        for row in rows:
            yield row
def query_see_pj(rut):
    """ Personajes del usuario """
    conn = None
    sql = """SELECT personaje_id, nombre, (select nombre from Razas, Personaje where razas_id = Personaje.id_raza) from Personaje where rut = %s;"""
    try:

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql,(rut,))
        for row in iter_row(cur):
            verificar= row
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def query_3(rut):
    """pasword de rut"""
    conn = None
    sql = """SELECT password,
             FROM Usuarios
             WHERE Usuarios.rut = %s;"""
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql,(rut,))
        for row in iter_row(cur):
            verificar= row
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
