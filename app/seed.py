
from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""

insert into Usuarios (rut) values (197808497, 200963296, 186389760, 195014612);
insert into Usuarios (nombre) values ('Joaquin Morales', 'Maria Lopez', 'Diego Becerra', 'Nicolas Ramirez');
insert into Usuarios (edad) values (21, 18, 24, 20);
insert into Usuarios (nickname) values ('Zaeta', 'Renacuajo', 'Kopa', 'Nick9a');
insert into Usuarios (direccion) values ('Barrio jeronimo', 'Jovino Novoa', 'Aromo de Castilla', 'Huasco');
insert into Usuarios (GM) values (false, false, true, false);

insert into Game_master (id_gm) values (1);
insert into Game_master (apodo) values ('Kopa');
insert into Game_master (rut_usuario) values (186389760);

insert into Personajes (nombre) values ('Illysaele', 'Sabaki', 'Tsun gu', 'Cid el feo');
insert into Personajes (rut_usuario) values (197808497, 200963296, 186389760, 195014612);
insert into Personajes (id_raza) values (5, 5, 8, 1);
insert into Personajes (id_clase) values (11, 1, 3, 8);
insert into Personajes (id_campana) values(1, 1, 1, 1);
insert into Personajes (nivel_clase) values(1,1,1,1);
insert into Personajes (Fuerza) values(20, 12, 13, 14);
insert into Personajes (Destreza) values(20, 12 , 14 ,11);
insert into Personajes (Constitucion) values(20, 12, 14, 11);
insert into Personajes (Inteligencia) values(1, 12, 13, 14);
insert into Personajes (Sabiduria) values(20, 13, 14, 10);
insert into Personajes (Carisma) values(20, 11, 12, 13);

insert into Campana (nombre_campana) values('Kono subarashii sekai ni shukufuku wo!');
insert into Campana (cantidad_jugadores) values(4);
insert into Campana (id_game_master) values(1);



"""
cur.execute(sql)

conn.commit()
post_id = cur.fetchone()[0]

print post_id


sql ="""insert INTO categorias_posts (categoria_id,post_id)
(SELECT id,%i  FROM categorias where nombre = 'Cine' or 
 nombre = 'Geek' or 
  nombre = 'Mundo Marvel'
);"""%(post_id)

cur.execute(sql)


conn.commit()
cur.close()
conn.close()
