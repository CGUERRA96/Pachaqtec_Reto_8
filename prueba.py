from controllers.prestamos_controller import Prestamo_controller
from datetime import datetime
from helpers.menu import Menu

class Stock:
    def __init__(self):
        self.prestamo = Prestamo_controller()


prueba = Stock()
prueba.prestamo.stock_prestado_libro(2)

