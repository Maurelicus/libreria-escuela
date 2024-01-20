SELECT
	alu.Usuario AS [Alumno],
	lib.Titulo AS [Libro(s) prestado],
	pl.Fecha,
	pl.Situacion
FROM
	pedido_libro AS pl
INNER JOIN
	libros AS lib
ON
	pl.LibroId = lib.LibroId
INNER JOIN
	alumnos AS alu
ON
	alu.EstudianteId = pl.UsuarioId