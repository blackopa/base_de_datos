
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

insert into Razas (1) values('Enano', 'Enano de las colinas', '+2 Con +1 Sab', +1 Golpe por nivel')
insert into Razas (1) values('Enano', 'Enano de las montanas', '+2 Con +2 Fue', 'Competencia armadura lig y pes')

insert into Razas (2) values('Elfo', 'Alto Elfo', '+2 Des +1 Int', 'Vision en la oscuridad, sentidos agudos') 
insert into Razas (2) values('Elfo', 'Elfo de los bosques', '+2 Des +1 Sab', 'Mascara de la naturaleza')
insert into Razas (2) values('Elfo', 'Elfo oscuro', '+2 Des +1 Car', 'Magia Drow')

insert into Razas (3) values('Mediano', 'Piesligeros', '+2 Des +1 Car', 'Sigiloso por Naturaleza')
insert into Razas (3) values('Mediano', 'Fornido', '+2 Des +1 Con', 'Resistencia de Fornido')

insert into Razas (4) values('Humano', 'Humankind', '+1 Fue +1 Con +1 Car +1 Des +1 Sab +1 Int', 'Competencia y dote a eleccion')

insert into Razas (5) values('Draconido', 'Linaje', '+2 Fue +1 Car', 'Linaje draconido')

insert into Razas (6) values('Gnomo', 'Gnomo de los bosques', '+2 Int +1 Des', 'Hablar con las Bestezuelas')
insert into Razas (6) values('Gnomo', 'Gnomo de las rocas', '+2 Int +1 Con', 'Saber del Artificiero, Manitas')

insert into Razas (7) values('Semielfo', 'De dos mundos', '+2 Car +1x2 a eleccion', 'Linaje Feerico, Versatil con habilidades')

insert into Razas (8) values('Semiorco', 'Gruumsh', '+2 Fue +1 Con', 'Amenazador, Aguante incansable, Ataques salvajes')

insert into Razas (9) values('Tiefling', 'Infernal', '+2 Car +1 Int', 'Resistencia infernal, Linaje Infernal')


insert into Clases (1) values('Barbaro', 'd12', 'Fuerza',
insert into Clases (2) values('Bardo', 'd8', 'Carisma',
insert into Clases (3) values('Brujo', 'd8', 'Carisma',
insert into Clases (4) values('Clerigo', 'd8', 'Sabiduria',
insert into Clases (5) values('Druida', 'd8', 'Sabiduria',
insert into Clases (6) values('Explorador', 'd10', 'Destreza y Sabiduria',
insert into Clases (7) values('Guerrero', 'd10', 'Fuerza o Destreza',
insert into Clases (8) values('Hechicero', 'd6', 'Carisma',
insert into Clases (9) values('Mago', 'd6', 'Inteligencia',
insert into Clases (10) values('Monje', 'd8', 'Destreza y Sabiduria',
insert into Clases (11) values('Paladin', 'd10', 'Fuerza y Carisma',
insert into Clases (12) values('Picaro', 'd8', 'Destreza', 

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
