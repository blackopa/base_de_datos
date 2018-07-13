#!/usr/bin/python

import psycopg2
from config import config
def insert_Usuarios(rut,Nombre,edad,nickname,direccion, Game_master, password):
    """ Insertar un usuario en la tabla Usuarios """
    sql = """INSERT INTO Usuarios(rut,Nombre,edad,nickname,direccion, Game_master, password)
             VALUES(%s, %s,%s,%s,%s,%s,%s);"""
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (rut,Nombre,edad,nickname,direccion, Game_master, password))
      
    
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return 
def insert_Personaje(nombre,rut_usuario,id_raza,id_clase,id_campana,nivel_de_clase,Fuerza,Destreza,Constitucion,Inteligencia,Sabiduria,Carisma):
	"""Insertar un personaje en la tabla personaje"""
	sql="""INSERT INTO Personaje(nombre,rut_usuario,id_raza,id_clase,id_campana,nivel_de_clase,Fuerza,Destreza,Constitucion,Inteligencia,Sabiduria,Carisma) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
	conn= None	
	try:
	params = config()
	conn = psycopg2.connect(**params)
	cur = conn.cursor()
	cur.execute(sql,(nombre,rut_usuario,id_raza,id_clase,id_campana,nivel_de_clase,Fuerza,Destreza,Constitucion,Inteligencia,Sabiduria,Carisma)
	
	conn.commit()
	cur.close()
	 except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
return

