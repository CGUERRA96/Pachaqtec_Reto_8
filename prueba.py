#Es necesario importar las depencendias necesarias
from datetime import date
from datetime import datetime

#Día actual
today = date.today()

#Fecha actual
now = datetime.now()

fecha_ahora = now.strftime("%d-%m-%y %H:%M")

print(today)
print(now)
print(fecha_ahora)