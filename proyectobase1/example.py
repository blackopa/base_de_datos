import psycopg2

try:
    conn = psycopg2.connect("dbname='test' user='testuser' host='localhost' password='123'")
    print ("conexion exitosa")
except:
    print ("no conecto")
cur = conn.cursor()
cur.execute("""SELECT datname from pg_database""")
rows = cur.fetchall()
print ("\nListado de bases de datos en el PC:\n")
for row in rows:
    print ("   ", row[0])
