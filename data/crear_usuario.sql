CREATE TABLE "usuarios" (
	"UsuarioId"	NVARCHAR(20) NOT NULL,
	"Usuario"	NVARCHAR(50),
	"Sexo"	NVARCHAR(10),
	"Nivel"	NVARCHAR(20),
	"Grado"	NVARCHAR(10),
	"Seccion"	NVARCHAR(4),
	"Tipo"	NVARCHAR(20),
	PRIMARY KEY("UsuarioId")
)