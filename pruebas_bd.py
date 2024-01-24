from conexion_sqlite import Comunicacion
from datetime import date, datetime

bd = Comunicacion()

today = date.today()
now = datetime.now()
print(today)
# print(now)

total=4
c_pedida=5
c_restante=total-c_pedida
if total==0:
    print('no hay existentes')
elif c_restante < 0:
    print('cantidad exedida')
else:
    print('correcto')