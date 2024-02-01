SELECT
	pl.LibroId,
	lib.cantidad
FROM
	pedido_libro AS pl
INNER JOIN
	libros AS lib
ON
	pl.LibroId = lib.LibroId
WHERE
	PedidoId=2