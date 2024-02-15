import sqlite3

class Comunicacion():
    
    def __init__(self):
        self.bd = sqlite3.connect("data/BDprueba.db")
    #! LIBROS
    def update_libros(self, idlibro, remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad, tipo):
        cursor = self.bd.cursor()
        query = '''
        UPDATE libros
        SET Remitente = '{}', AñoRecepcion = '{}', NivelEducativo = '{}', Titulo = '{}', Autor = '{}', Editorial = '{}', AñoEdicion = '{}', CondicionLibro = '{}', Cantidad = '{}', Tipo = '{}'
        WHERE LibroId = '{}'
        '''.format(remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad, tipo, idlibro)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def show_libros(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT 
            li.Remitente,
            li.AñoRecepcion,
            li.NivelEducativo,
            li.Titulo,
            li.Autor,
            li.Editorial,
            li.AñoEdicion,
            li.CondicionLibro,
            li.Cantidad,
            li.LibroId,
			ca.Categoria
        FROM 
            libros AS li
		LEFT OUTER JOIN
			categorias AS ca
		ON
			li.Tipo = ca.TipoId
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def append_libro(self, remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad, tipo):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO libros (Remitente, AñoRecepcion, NivelEducativo, Titulo, Autor, Editorial, AñoEdicion, CondicionLibro, Cantidad, Tipo)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')
        '''.format(remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad, tipo)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()

    def delete_libro(self, id):
        cursor = self.bd.cursor()
        query = '''
        DELETE FROM libros
        WHERE LibroId = '{}'        
        '''.format(id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def search_libros(self, columna, palabra):
        cursor = self.bd.cursor()
        query = '''
        SELECT 
            li.Remitente AS [Remitente],
            li.AñoRecepcion AS [AñoRecepcion],
            li.NivelEducativo AS [NivelEducativo],
            li.Titulo AS [Titulo],
            li.Autor AS [Autor],
            li.Editorial AS [Editorial],
            li.AñoEdicion AS [AñoEdicion],
            li.CondicionLibro AS [CondicionLibro],
            li.Cantidad AS [Cantidad],
            li.LibroId,
			ca.Categoria AS [Categoria]
        FROM 
            libros AS li
		LEFT OUTER JOIN
			categorias AS ca
		ON
			li.Tipo = ca.TipoId
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    #! LAMINAS
    def show_laminas(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            la.Remitente,
            la.AñoRecepcion,
            la.NivelEducativo,
            la.Titulo,
            la.CondicionLamina,
            la.Codigo,
            la.Cantidad,
            la.LaminasId,
            ca.Categoria
        FROM 
            laminas AS la
        LEFT OUTER JOIN
            categorias AS ca
        ON
            la.TipoId = ca.TipoId
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def delete_lamina(self, id):
        cursor = self.bd.cursor()
        query = '''
        DELETE FROM laminas
        WHERE LaminasId = '{}'        
        '''.format(id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def update_lamina(self, idlamina, codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad, tipo):
        cursor = self.bd.cursor()
        query = '''
        UPDATE laminas
        SET Codigo = '{}', Remitente = '{}', AñoRecepcion = '{}', NivelEducativo = '{}', Titulo = '{}', CondicionLamina = '{}', Cantidad = '{}', TipoId = '{}'
        WHERE LaminasId = '{}'
        '''.format(codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad, tipo, idlamina)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def append_lamina(self, codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad, tipo):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO laminas (Codigo, Remitente, AñoRecepcion, NivelEducativo, Titulo, CondicionLamina, Cantidad, TipoId)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}')
        '''.format(codigo, remitente, año_recepcion, nivel_educativo, titulo, condicion_lamina, cantidad, tipo)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def search_laminas(self, columna, palabra):
        cursor = self.bd.cursor()
        query = '''
        SELECT 
            la.Remitente AS [Remitente],
            la.AñoRecepcion AS [AñoRecepcion],
            la.NivelEducativo AS [NivelEducativo],
            la.Titulo AS [Titulo],
            la.CondicionLamina AS [CondicionLamina],
            la.Codigo AS [Codigo],
            la.Cantidad AS [Cantidad],
            la.LaminasId,
            ca.Categoria AS [Categoria]
        FROM 
            laminas AS la
        LEFT OUTER JOIN
            categorias AS ca
        ON
            la.TipoId = ca.TipoId
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    #! ALUMNO
    def show_alumnos(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            Alumno,
            Sexo,
            Nivel,
            Grado,
            Seccion,
            Codigo,
            AlumnoId,
            Tipo
        FROM 
            alumnos
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def append_alumno(self, codigo, alumno, sexo, nivel, grado, seccion, tipo):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO alumnos (Codigo, Alumno, Sexo, Nivel, Grado, Seccion, Tipo) 
        VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}")
        '''.format(codigo, alumno, sexo, nivel, grado, seccion, tipo)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    
    def update_alumno(self, idalumno, codigo, alumno, sexo, nivel, grado, seccion):
        cursor = self.bd.cursor()
        query = '''
        UPDATE Alumnos
        SET Codigo = '{}', Alumno = '{}', Sexo = '{}', Nivel = '{}', Grado = '{}', Seccion = '{}'
        WHERE AlumnoId = '{}'
        '''.format(codigo, alumno, sexo, nivel, grado, seccion, idalumno)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def delete_alumno(self, Alumnoid):
        cursor = self.bd.cursor()
        query = '''
        DELETE FROM alumnos
        WHERE AlumnoId = '{}'        
        '''.format(Alumnoid)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def search_alumnos(self, columna, palabra):
        cursor = self.bd.cursor()
        query = '''
        SELECT 
            Alumno,
            Sexo,
            Nivel,
            Grado,
            Seccion,
            Codigo,
            AlumnoId,
            Tipo
        FROM 
            alumnos
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        try:
            cursor.execute(query)
            l_filas = cursor.fetchall()
            return l_filas
        except sqlite3.OperationalError:
            print("incorrecto")
    
    #! PEDIDO
    def append_pedido(self, codigo, libroid, alumnoid, fecha, situacion, observacion, cantidad):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO pedido_libro_alumno (Codigo, LibroId, AlumnoId, FechaSalida, Situacion, Observacion, Cantidad)
        VALUES('{}','{}','{}','{}','{}','{}','{}')
        '''.format(codigo, libroid, alumnoid, fecha, situacion, observacion, cantidad)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def update_libro_cantidad(self, libroid, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE libros
        SET Cantidad = '{}'
        WHERE LibroId = '{}'
        '''.format(cantidad, libroid)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    #! DEVOLUCIONES
    def show_pedidos(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            alu.Alumno,
            lib.Titulo,
            pl.Observacion,
            pl.FechaSalida,
            pl.FechaEntrada,
            pl.Situacion,
            pl.Cantidad,
            pl.PedidoId,
            pl.Codigo,
            pl.LibroId,
            pl.AlumnoId
        FROM
            pedido_libro_alumno AS pl
        INNER JOIN
            libros AS lib
        ON
            pl.LibroId = lib.LibroId
        INNER JOIN
            alumnos AS alu
        ON
            alu.AlumnoId = pl.AlumnoId
        ORDER BY
            pl.Situacion
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def buscar_pedidos(self, columna, palabra):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            alu.Alumno AS [Alumno],
            lib.Titulo AS [Libro],
            pl.Observacion,
            pl.FechaSalida AS [Fecha],
            pl.FechaEntrada,
            pl.Situacion AS [Situacion],
            pl.Cantidad,
            pl.PedidoId
        FROM
            pedido_libro_alumno AS pl
        INNER JOIN
            libros AS lib
        ON
            pl.LibroId = lib.LibroId
        INNER JOIN
            alumnos AS alu
        ON
            alu.AlumnoId = pl.AlumnoId
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def info_pedidolibro(self, pedidoid):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            pl.LibroId,
            lib.Cantidad,
            pl.AlumnoId,
            pl.FechaSalida
        FROM
            pedido_libro_alumno AS pl
        INNER JOIN
            libros AS lib
        ON
            pl.LibroId = lib.LibroId
        WHERE 
            PedidoId = {}
        '''.format(pedidoid)
        cursor.execute(query)
        idlibro = cursor.fetchall()
        return idlibro
        
    def agregar_pedido(self, codigo, libroid, alumnoid, fecha_s, fecha_e, situacion, observacion, cantidad):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO pedido_libro_alumno (Codigo, LibroId, UsuarioId, FechaSalida, FechaEntrada, Situacion, Observacion, Cantidad)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}')
        '''.format(codigo, libroid, alumnoid, fecha_s, fecha_e, situacion, observacion, cantidad)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def update_pedido(self, pedidoid, fecha_devolucion, situacion, observacion, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE pedido_libro_alumno
        SET FechaEntrada = '{}', Situacion = '{}', Observacion = '{}', Cantidad = '{}'
        WHERE PedidoId = '{}'
        '''.format(fecha_devolucion, situacion, observacion, cantidad, pedidoid)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()

    def show_categorias(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            Categoria
        FROM
            categorias
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
        