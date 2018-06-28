
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
insert into Usuarios (password) values('7473177j', '200963296', 'koala123', 'nose123');

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
insert into Personajes (Inteligencia) values(20, 12, 13, 14);
insert into Personajes (Sabiduria) values(20, 13, 14, 10);
insert into Personajes (Carisma) values(20, 11, 12, 13);

insert into Campana (nombre_campana) values('Kono subarashii sekai ni shukufuku wo!');
insert into Campana (cantidad_jugadores) values(4);
insert into Campana (id_game_master) values(1);

insert into Razas (nombre) values('Enano','Enano','Elfo', 'Elfo', 'Elfo', 'Mediano', 'Mediano', 'Humano', 'Draconido', 'Gnomo', 'Gnomo', 'Semielfo', 'Semiorco', 'Semielfo', 'Tiefling');
insert into Razas (subraza) values('Enano de las colinas', 'Enano de las montanas', 'Alto Elfo', 'Elfo de los bosques', 'Elfo oscuro', 'Piesligeros', 'Fornido', 'Humano', 'Linaje', 'Gnomo de los bosques', 'Gnomo de las rocas', 'De dos mundos', 'Gruumsh', 'Infernal');
insert into Razas (Aumento_atributo) values('+2 Con +1 Sab', '+2 Con +2 Fue', '+2 Des +1 Int', '+2 Des +1 Sab', '+2 Des +1 Car', '+2 Des +1 Car', '+2 Des +1 Con', '+2 Fue +1 Car',  '+1 Fue +1 Con +1 Car +1 Des +1 Sab +1 Int', '+2 Int +1 Des', '+2 Int +1 Con', '+2 Car +1x2 a eleccion', '+2 Fue +1 Con', '+2 Car +1 Int');
insert into Razas (habilidad_raza) values('+1 Golpe por nivel', 'Competencia armadura lig y pes', 'Vision en la oscuridad, sentidos agudos', 'Mascara de la naturaleza', 'Magia Drow', 'Sigiloso por Naturaleza', 'Resistencia de Fornido', 'Competencia y dote a eleccion', 'Linaje draconido', 'Hablar con las Bestezuelas', 'Saber del Artificiero, Manitas', 'Linaje Feerico, Versatil con habilidades', 'Amenazador, Aguante incansable, Ataques salvajes', 'Resistencia infernal, Linaje Infernal'); 

insert into Clases (nombre) values('Barbaro', 'Bardo', 'Brujo', 'Clerigo', 'Druida', 'Explorador', 'Guerrero', 'Hechicero', 'Mago', 'Monje', 'Paladin, 'Picaro');
insert into Clases (dado_golpe) values('d12', 'd8', 'd8', 'd8', 'd8', 'd10', 'd10', 'd6', 'd6', 'd8', 'd10', 'd8');
insert into Clases (atributo_adepto) values('Fuerza', 'Carisma', 'Carisma', 'Sabiduria', 'Sabiduria', 'Destreza y Sabiduria', 'Fuerza o Destreza', 'Carisma', 'Inteligencia', 'Destreza y Sabiduria', 'Fuerza y Carisma', 'Destreza');

insert into Objetos (nombre) values('Baston', 'Daga', Garrote', 'Garrote grande', 'Hacha de mano', 'Hoz', 'Jabalina', 'Lanza', 'Martillo ligero', 'Maza');
insert into Objetos (descripcion) values('1d6 Contudente', '1d4 Perforante', '1d4 Contundente', '1d8 Contundente', '1d6 Cortante', '1d4 Cortante', '1d6 Perforante', '1d6 Perforente', '1d4 Contundente', '1d6 Contundente');

insert into Objetos (nombre) values('Arco corto', 'Ballesta ligera', 'Dardo', 'Honda');
insert into Objetos (descripcion) values('1d6 Perforante', '1d8 Perforante', '1d4 Perforante', '1d4 Contundente');

insert into Objetos (nombre) values('Alabarda', 'Cimitarra', 'Espada corta', 'Espada larga', 'Espadon', 'Estoque', 'Flagelo', 'Guja', 'Hacha a dos manos', 'Hacha de guerra', 'Lanza de caballeria', 'Latigo', 'Lucero del alba', 'Martillo de guerra', 'Maza a dos manos', 'Pica', 'Pico de guerra', 'Tridente');
insert into Objetos (descripcion) values('1d10 Cortante ¡La mejor arma de todas!', '1d6 Cortante', '1d6 Perforante', '1d8 Cortante', '2d6 Cortante', '1d8 Perforante', '1d8 Contudente', '1d10 Cortante', '1d12 Cortante', '1d8 Cortante', '1d12 Perforante', '1d4 Cortante', '1d8 Perforante', '1d8 Contundente', '2d6 Contundente', '1d10 Perforante', '1d8 Perforante', '1d6 Perforante');

insert into Objetos (nombre) values('Arco largo', 'Ballesta de mano', 'Ballesta pesada', 'cerbatana', 'Red');
insert into Objetos (descripcion) values('1d8 Perforante', '1d6 Perforante', '1d10 Perforante', '1 Perforante', '¿De verdad crees que esto hace daño?');



insert into hechizos (nombre) values('Amistad', 'Burla dañina', 'Caida de pluma', 'Curar heridas', 'Abrir', 'Boca magica', 'Clarividencia', 'Crecimiento vegetal', 'Compulsion', 'Confusion', 'Alterar los recuerdos', 'Alzar a los muertos', 'Baile irresistible de Otto', 'Encontrar el camino', 'Espada de Mordenkainen', 'Dominar monstruo', 'Labia', 'Palabra de poder: matar', 'Palabra de poder: sanar');
insert into hechizos (nivel_hechizo) values(0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9);



"""
cur.execute(sql)
sql ="""
insert into Objeto (nombre,descripcion) values ('Baston','1d6 Contundente') returning id;
"""
cur.execute(sql)
conn.commit()
objeto_id = cur.fetchone()[0]

print objeto_id

sql ="""insert INTO Inventario (personaje_id,objeto_id,cantidad)
(SELECT id,%i,2  FROM Personaje,Usuario where Personaje.nombre = 'Tsun gu' and Usuarios.nickname='Kopa';
);"""%(objeto_id)

cur.execute(sql)


conn.commit()
cur.close()
conn.close()
