from conexion_sqlite import Comunicacion

bd = Comunicacion()

l_datos = bd.buscador2()
print(l_datos)