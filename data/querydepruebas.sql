SELECT
	alu.Usuario AS [Alumno],
	lib.Titulo AS [Libro],
	pl.Observacion,
	pl.Fecha,
	pl.Situacion,
	pl.Cantidad,
	pl.PedidoId
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
