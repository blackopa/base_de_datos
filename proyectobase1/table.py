from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


cur = conn.cursor()
sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql ="""
CREATE TABLE Usuarios
           (rut integer PRIMARY KEY, Nombre varchar(40), edad integer, nickname varchar(20), direccion varchar(72), Game_master boolean, password varchar(20));
"""

cur.execute(sql)


sql ="""
CREATE TABLE Personaje 
           (personaje_id serial PRIMARY KEY, nombre varchar(40), rut_usuario integer, id_raza integer, id_clase integer, id_campana integer ,nivel_de_clase integer, Fuerza integer, Destreza integer, Constitucion integer, Inteligencia integer, Sabiduria integer, Carisma integer);
"""

cur.execute(sql)

sql ="""
CREATE TABLE Campana
           (campana_id serial PRIMARY KEY, nombre_campana varchar(40), cantidad_jugadores integer, id_game_master integer);
"""

cur.execute(sql)

sql ="""
CREATE TABLE  Game_master
           (Game_master_id serial PRIMARY KEY,apodo varchar(40),rut_usuario integer);
"""

cur.execute(sql)

sql ="""
CREATE TABLE Razas
           (razas_id serial PRIMARY KEY, nombre varchar(140), subraza varchar(40),Aumento_atributo varchar(40),habilidad_raza varchar(100));
"""

cur.execute(sql)

sql ="""
CREATE TABLE Clases
           (clase_id serial PRIMARY KEY, nombre varchar(140), dado_golpe varchar(40),atributo_adepto varchar(40),id_tabla_nivel integer);
"""

cur.execute(sql)

sql ="""
CREATE TABLE Tabla_niveles
           (Tabla_id serial PRIMARY KEY,id_clase integer,nombre varchar(40), bono_proficiencia integer ,Habilidad_nivel varchar(140),hechizos_nivel integer,nivel integer);
"""

sql ="""
CREATE TABLE Objetos
           (objeto_id serial PRIMARY KEY, nombre varchar(140),descripcion varchar(300));
"""

cur.execute(sql)
sql=Â"""
CREATE TABLE Inventario
	(id_personaje integer,id_objeto integer,cantidad integer);
cur.execute(sql)
sql =""
CREATE TABLE hechizos
           (Hechizo_id serial PRIMARY KEY, nombre varchar(140), nivel_hechizo integer,Descripcion varchar(300));
"""
cur.execute(sql)
sql ="""
CREATE TABLE Libro
	(id_hechizo integer,id_personaje integer);
"""
cur.execute(sql)
sql ="""
CREATE TABLE Historial_campana
           (campana_id integer,usuario_id integer );
"""
cur.execute(sql)
conn.commit()
cur.close()
conn.close()

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
