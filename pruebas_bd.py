from conexion_sqlite import Comunicacion
from datetime import date, datetime

bd = Comunicacion()

today = date.today()
now = datetime.now()
print(today)
print(now)

# format = now.strftime('Día :%d, Mes: %m, Año:%Y, Hora:%H, Minutos: %M, Segundos: %S')
format = now.strftime('%Y-%m-%d')
print(format)
# numero=
canti=bd.cantidad(89)
print(canti[0])
print(canti[0][0]-9)
# print(canti)