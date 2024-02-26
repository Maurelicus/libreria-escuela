import sqlite3

class Comunicacion():
    
    def __init__(self):
        self.bd = sqlite3.connect("data/BDprueba.db")
    #! LIBROS 6
    def show_libros(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            li.Titulo,
            li.Autor,
            li.Editorial,
            li.AñoEdicion,
			ca.Categoria,
            li.Cantidad,
            li.Remitente,
            li.NivelEducativo,
            li.CondicionLibro,
            li.AñoRecepcion,
            li.LibroId
        FROM 
            libros AS li
		LEFT OUTER JOIN
			categorias AS ca
		ON
			li.Tipo = ca.TipoId
        ORDER BY
            li.NivelEducativo DESC
        '''
        """ 
            li.Tipo,
            li.Titulo ASC
            li.Cantidad DESC,
            li.Editorial
        """
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def update_libros(
            self, idlibro, remitente, año_recepcion, nivel_educativo, 
            titulo, autor, editorial, año_edicion, condicion_libro, 
            cantidad, tipo):
        cursor = self.bd.cursor()
        query = '''
            UPDATE 
                libros
            SET 
                Remitente = '{}', AñoRecepcion = '{}', 
                NivelEducativo = '{}', Titulo = '{}', Autor = '{}', 
                Editorial = '{}', AñoEdicion = '{}', 
                CondicionLibro = '{}', Cantidad = '{}', Tipo = '{}'
            WHERE 
                LibroId = '{}'
            '''.format(remitente, año_recepcion, nivel_educativo, titulo, autor, editorial, año_edicion, condicion_libro, cantidad, tipo, idlibro)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
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
            li.Titulo AS [Titulo],
            li.Autor AS [Autor],
            li.Editorial AS [Editorial],
            li.AñoEdicion AS [AñoEdicion],
			ca.Categoria AS [Categoria],
            li.Cantidad AS [Cantidad],
            li.Remitente AS [Remitente],
            li.NivelEducativo AS [NivelEducativo],
            li.CondicionLibro AS [CondicionLibro],
            li.AñoRecepcion AS [AñoRecepcion],
            li.LibroId
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
    #! LAMINAS 6
    def show_laminas(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            la.Titulo,
            ca.Categoria,
            la.Codigo,
            la.Cantidad,
            la.Remitente,
            la.CondicionLamina,
            la.NivelEducativo,
            la.AñoRecepcion,
            la.LaminasId
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
    def delete_lamina(self, id):
        cursor = self.bd.cursor()
        query = '''
        DELETE FROM laminas
        WHERE LaminasId = '{}'        
        '''.format(id)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def search_laminas(self, columna, palabra):
        cursor = self.bd.cursor()
        query = '''
        SELECT 
            la.Titulo AS [Titulo],
            ca.Categoria AS [Categoria],
            la.Codigo AS [Codigo],
            la.Cantidad AS [Cantidad],
            la.Remitente AS [Remitente],
            la.CondicionLamina AS [CondicionLamina],
            la.NivelEducativo AS [NivelEducativo],
            la.AñoRecepcion AS [AñoRecepcion],
            la.LaminasId
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
    
    def update_lamina_cantidad(self, laminaid, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE laminas
        SET Cantidad = '{}'
        WHERE LaminasId = '{}'
        '''.format(cantidad, laminaid)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()

    #! ALUMNO 5
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
            Tipo
        FROM 
            alumnos
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def update_alumno(self, idalumno, n_codigo, alumno, sexo, nivel, grado, seccion):
        cursor = self.bd.cursor()
        query = '''
        UPDATE alumnos
        SET Codigo = '{}', Alumno = '{}', Sexo = '{}', Nivel = '{}', Grado = '{}', Seccion = '{}'
        WHERE Codigo = '{}'
        '''.format(n_codigo, alumno, sexo, nivel, grado, seccion, idalumno)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()

    def delete_alumno(self, Alumnoid):
        cursor = self.bd.cursor()
        query = '''
        DELETE FROM alumnos
        WHERE Codigo = '{}'        
        '''.format(Alumnoid)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def append_alumno(self, codigo, alumno, sexo, nivel, grado, seccion, tipo):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO alumnos (Codigo, Alumno, Sexo, Nivel, Grado, Seccion, Tipo) 
        VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}")
        '''.format(codigo, alumno, sexo, nivel, grado, seccion, tipo)
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
#! PROFESOR 5
    def show_profesores(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            Profesor,
            CorreoElectronico,
            Celular,
            Codigo,
            Tipo
        FROM 
            profesores
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def update_profesor(self, idprofesor, n_codigo, profesor, correo, celular):
        cursor = self.bd.cursor()
        query = '''
        UPDATE profesores
        SET Codigo = '{}', Profesor = '{}', CorreoElectronico = '{}', Celular = '{}'
        WHERE Codigo = '{}'
        '''.format(n_codigo, profesor, correo, celular, idprofesor)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def delete_profesor(self, profesorid):
        cursor = self.bd.cursor()
        query = '''
        DELETE FROM profesores
        WHERE Codigo = '{}'        
        '''.format(profesorid)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def append_profesor(self, codigo, profesor, correo, celular, tipo):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO profesores (Codigo, Profesor, CorreoElectronico, Celular, Tipo) 
        VALUES ("{}", "{}", "{}", "{}", "{}")
        '''.format(codigo, profesor, correo, celular, tipo)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def search_profesores(self, columna, palabra):
        cursor = self.bd.cursor()
        query = '''
        SELECT 
            Profesor,
            CorreoElectronico,
            Celular,
            Codigo,
            Tipo
        FROM 
            profesores
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        try:
            cursor.execute(query)
            l_filas = cursor.fetchall()
            return l_filas
        except sqlite3.OperationalError:
            print("incorrecto")
    #!  PEDIDO ALUMNO-LIBRO
    def showalu_pedidoslib(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            lib.Titulo,
            alu.Alumno,
            pl.FechaSalida,
            pl.FechaEntrada,
            pl.Cantidad,
            pl.Situacion,
            pl.Observacion,
            pl.Codigo,
            pl.PedidoId,
            pl.LibroId,
            pl.AlumnoId,
            pl.Tipo
        FROM
            pedido_libro_alumno AS pl
        LEFT OUTER JOIN
            libros AS lib
        ON
            pl.LibroId = lib.LibroId
        LEFT OUTER JOIN
            alumnos AS alu
        ON
            alu.Codigo = pl.AlumnoId
        ORDER BY
            pl.Situacion
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def buscaralu_pedidoslib(self, columna, palabra):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            lib.Titulo AS [Libro],
            alu.Alumno AS [Alumno],
            pl.FechaSalida AS [Fecha],
            pl.FechaEntrada,
            pl.Cantidad,
            pl.Situacion AS [Situacion],
            pl.Observacion,
            pl.Codigo,
            pl.PedidoId,
            pl.LibroId,
            pl.AlumnoId,
            pl.Tipo
        FROM
            pedido_libro_alumno AS pl
        INNER JOIN
            libros AS lib
        ON
            pl.LibroId = lib.LibroId
        INNER JOIN
            alumnos AS alu
        ON
            alu.Codigo = pl.AlumnoId
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def appendalu_pedidolib(self, codigo, libroid, alumnoid, fecha_s,fecha_e, situacion, observacion, cantidad, tipo):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO pedido_libro_alumno (Codigo, LibroId, AlumnoId, FechaSalida,FechaEntrada, Situacion, Observacion, Cantidad, Tipo)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')
        '''.format(codigo, libroid, alumnoid, fecha_s,fecha_e, situacion, observacion, cantidad, tipo)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def updatealu_pedidolib(self, pedidoid, fecha_devolucion, situacion, observacion, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE pedido_libro_alumno
        SET FechaEntrada = '{}', Situacion = '{}', Observacion = '{}', Cantidad = '{}'
        WHERE PedidoId = '{}'
        '''.format(fecha_devolucion, situacion, observacion, cantidad, pedidoid)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def infoalu_pedidolib(self, pedidoid):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            lib.Cantidad
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
    #!  PEDIDO PROFESOR-LIBRO
    def showpro_pedidoslib(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            lib.Titulo,
            pro.Profesor,
            pl.FechaSalida,
            pl.FechaEntrada,
            pl.Cantidad,
            pl.Situacion,
            pl.Observacion,
            pl.Codigo,
            pl.PedidoId,
            pl.LibroId,
            pl.ProfesorId,
            pl.Tipo
        FROM
            pedido_libro_profesor AS pl
        INNER JOIN
            libros AS lib
        ON
            pl.LibroId = lib.LibroId
        INNER JOIN
            profesores AS pro
        ON
            pro.Codigo = pl.ProfesorId
        ORDER BY
            pl.Situacion
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def buscarpro_pedidoslib(self, columna, palabra):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            lib.Titulo AS [Libro],
            pro.Profesor AS [Profesor],
            pl.FechaSalida AS [Fecha],
            pl.FechaEntrada,
            pl.Cantidad,
            pl.Situacion AS [Situacion],
            pl.Observacion,
            pl.Codigo,
            pl.PedidoId,
            pl.LibroId,
            pl.ProfesorId,
            pl.Tipo
        FROM
            pedido_libro_profesor AS pl
        INNER JOIN
            libros AS lib
        ON
            pl.LibroId = lib.LibroId
        INNER JOIN
            profesores AS pro
        ON
            pro.Codigo = pl.ProfesorId
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def appendpro_pedidolib(self, codigo, libroid, profesorid, fecha_s,fecha_e, situacion, observacion, cantidad, tipo):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO pedido_libro_profesor (Codigo, LibroId, ProfesorId, FechaSalida,FechaEntrada,Situacion,Observacion,Cantidad,Tipo)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')
        '''.format(codigo, libroid, profesorid, fecha_s,fecha_e, situacion, observacion, cantidad, tipo)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def updatepro_pedidolib(self, pedidoid, fecha_devolucion, situacion, observacion, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE pedido_libro_profesor
        SET FechaEntrada = '{}', Situacion = '{}', Observacion = '{}', Cantidad = '{}'
        WHERE PedidoId = '{}'
        '''.format(fecha_devolucion, situacion, observacion, cantidad, pedidoid)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    
    def infopro_pedidolib(self, pedidoid):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            lib.Cantidad
        FROM
            pedido_libro_profesor AS pl
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
        
    #!  PEDIDO ALUMNO-LAMINA
    def showalu_pedidoslam(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            lam.Titulo,
            alu.Alumno,
            pl.FechaSalida,
            pl.FechaEntrada,
            pl.Cantidad,
            pl.Situacion,
            pl.Observacion,
            lam.Codigo,
            pl.PedidoId,
            pl.LaminaId,
            pl.AlumnoId,
            pl.Tipo
        FROM
            pedido_lamina_alumno AS pl
        LEFT OUTER JOIN
            laminas AS lam
        ON
            pl.LaminaId = lam.LaminasId
        LEFT OUTER JOIN
            alumnos AS alu
        ON
            alu.Codigo = pl.AlumnoId
        ORDER BY
            pl.Situacion
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def buscaralu_pedidoslam(self, columna, palabra):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            lam.Titulo AS [Lamina],
            alu.Alumno AS [Alumno],
            pl.FechaSalida AS [Fecha],
            pl.FechaEntrada,
            pl.Cantidad,
            pl.Situacion AS [Situacion],
            pl.Observacion,
            lam.Codigo,
            pl.PedidoId,
            pl.LibroId,
            pl.AlumnoId,
            pl.Tipo
        FROM
            pedido_lamina_alumno AS pl
        INNER JOIN
            laminas AS lam
        ON
            pl.LaminaId = lam.LaminasId
        INNER JOIN
            alumnos AS alu
        ON
            alu.Codigo = pl.AlumnoId
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def appendalu_pedidolam(self, laminaid, alumnoid, fecha_s,fecha_e, situacion, observacion, cantidad, tipo):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO pedido_lamina_alumno (LaminaId, AlumnoId, FechaSalida,FechaEntrada, Situacion, Observacion, Cantidad, Tipo)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}')
        '''.format(laminaid, alumnoid, fecha_s,fecha_e, situacion, observacion, cantidad, tipo)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def infoalu_pedidolam(self, pedidoid):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            lam.Cantidad
        FROM
            pedido_lamina_alumno AS pl
        INNER JOIN
            laminas AS lam
        ON
            pl.LaminaId = lam.LaminasId
        WHERE 
            PedidoId = {}
        '''.format(pedidoid)
        cursor.execute(query)
        idlibro = cursor.fetchall()
        return idlibro
    
    def updatealu_pedidolam(self, pedidoid, fecha_devolucion, situacion, observacion, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE pedido_lamina_alumno
        SET FechaEntrada = '{}', Situacion = '{}', Observacion = '{}', Cantidad = '{}'
        WHERE PedidoId = '{}'
        '''.format(fecha_devolucion, situacion, observacion, cantidad, pedidoid)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    #!  PEDIDO PROFESOR-LAMINA
    def showpro_pedidoslam(self):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            lam.Titulo,
            pro.Profesor,
            pl.FechaSalida,
            pl.FechaEntrada,
            pl.Cantidad,
            pl.Situacion,
            pl.Observacion,
            lam.Codigo,
            pl.PedidoId,
            pl.LaminaId,
            pl.ProfesorId,
            pl.Tipo
        FROM
            pedido_lamina_profesor AS pl
        INNER JOIN
            laminas AS lam
        ON
            pl.LaminaId = lam.LaminasId
        INNER JOIN
            profesores AS pro
        ON
            pro.Codigo = pl.ProfesorId
        ORDER BY
            pl.Situacion
        '''
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def buscarpro_pedidoslam(self, columna, palabra):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            lam.Titulo AS [Lamina],
            pro.Profesor AS [Profesor],
            pl.FechaSalida AS [Fecha],
            pl.FechaEntrada,
            pl.Cantidad,
            pl.Situacion AS [Situacion],
            pl.Observacion,
            lam.Codigo,
            pl.PedidoId,
            pl.LaminaId,
            pl.ProfesorId,
            pl.Tipo
        FROM
            pedido_lamina_profesor AS pl
        INNER JOIN
            laminas AS lam
        ON
            pl.LaminaId = lam.LaminasId
        INNER JOIN
            profesores AS pro
        ON
            pro.Codigo = pl.ProfesorId
        WHERE 
            {} LIKE '%{}%'
        '''.format(columna,palabra)
        cursor.execute(query)
        l_filas = cursor.fetchall()
        return l_filas
    
    def appendpro_pedidolam(self, laminaid, profesorid, fecha_s,fecha_e, situacion, observacion, cantidad, tipo):
        cursor = self.bd.cursor()
        query = '''
        INSERT INTO pedido_lamina_profesor (LaminaId, ProfesorId, FechaSalida,FechaEntrada, Situacion, Observacion, Cantidad, Tipo)
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}')
        '''.format(laminaid, profesorid, fecha_s,fecha_e, situacion, observacion, cantidad, tipo)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def infopro_pedidolam(self, pedidoid):
        cursor = self.bd.cursor()
        query = '''
        SELECT
            lam.Cantidad
        FROM
            pedido_lamina_profesor AS pl
        INNER JOIN
            laminas AS lam
        ON
            pl.LaminaId = lam.LaminasId
        WHERE 
            PedidoId = {}
        '''.format(pedidoid)
        cursor.execute(query)
        idlibro = cursor.fetchall()
        return idlibro
        
    def updatepro_pedidolam(self, pedidoid, fecha_devolucion, situacion, observacion, cantidad):
        cursor = self.bd.cursor()
        query = '''
        UPDATE pedido_lamina_profesor
        SET FechaEntrada = '{}', Situacion = '{}', Observacion = '{}', Cantidad = '{}'
        WHERE PedidoId = '{}'
        '''.format(fecha_devolucion, situacion, observacion, cantidad, pedidoid)
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
    
    def eliminar_talumno(self):
        cursor = self.bd.cursor()
        query = '''
            drop table alumnos
        '''
        cursor.execute(query)
        self.bd.commit()
        cursor.close()
        
    def crear_talumno(self):
        cursor = self.bd.cursor()
        query = '''
            CREATE TABLE "alumnos" (
                "Alumno"	NVARCHAR(50) NOT NULL,
                "Sexo"	NVARCHAR(10),
                "Nivel"	NVARCHAR(20),
                "Grado"	NVARCHAR(10),
                "Seccion"	NVARCHAR(4),
                "Codigo"	NVARCHAR(20) NOT NULL UNIQUE,
                "Tipo"	NVARCHAR(10) NOT NULL,
                PRIMARY KEY("Codigo")
            )
        '''
        cursor.execute(query)
        self.bd.commit()
        cursor.close()