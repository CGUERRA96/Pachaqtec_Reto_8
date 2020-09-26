from connection.conn import Conexion

class Database:
    def __init__ (self, conn):
        self.conn = conn

    def crear_persona(self):        
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  personas(
                id_persona  SERIAL   PRIMARY KEY NOT NULL,
                dni_persona varchar(8) NOT NULL,
                nombres varchar(100) NOT NULL,
                apellidos varchar(50) NOT NULL,
                correo varchar(60) NOT NULL,
                telefono varchar(20) NOT NULL,
                direccion varchar(20) NOT NULL
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
        
    def crear_roles(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  roles(
                id_rol  SERIAL  PRIMARY KEY NOT NULL,
                tipo_rol varchar(25) NOT NULL,
                id_persona integer NOT NULL,
                FOREIGN KEY (id_persona) REFERENCES personas(id_persona)                
            );
        '''
        conn.ejecutar_sentencia(create_table_query)

    def crear_categoria_libro(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  categoria_libro(
                id_categoria  SERIAL  PRIMARY KEY NOT NULL,
                descripcion varchar(100) NOT NULL                
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
                
    def crear_libros(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  libros(
                id_libro  SERIAL  PRIMARY KEY NOT NULL,
                nombre varchar(100) NOT NULL,
                autor varchar(50) NOT NULL,
                id_categoria integer NOT NULL,
                editorial varchar(50) NOT NULL,
                anio_edicion varchar(4) NOT NULL,
                estado_libro varchar(20) NOT NULL DEFAULT 'disponible',
                FOREIGN KEY (id_categoria) REFERENCES categoria_libro(id_categoria) 
            );
        '''
        conn.ejecutar_sentencia(create_table_query)

    def crear_prestamo(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS  prestamo(
                id_prestamo SERIAL  PRIMARY KEY NOT NULL,
                id_lector integer NOT NULL,
                id_libro integer NOT NULL,
                fecha_solicitud date,
                id_administrador integer NOT NULL,
                fecha_prestamo date NOT NULL,
                plazo integer DEFAULT 3,
                fecha_devolucion date,
                estado_prestamo varchar(20) NOT NULL DEFAULT 'pendiente',
                estado_seguimiento varchar(20),
                FOREIGN KEY (id_lector) REFERENCES roles(id_rol),
                FOREIGN KEY (id_libro) REFERENCES libros(id_libro)
            );
        '''
        conn.ejecutar_sentencia(create_table_query)
                
    

conn = Conexion('sistema_biblioteca')
db= Database(conn)
db.crear_persona()
db.crear_roles()
db.crear_categoria_libro()
db.crear_libros()
db.crear_prestamo()
conn.close_connection()
