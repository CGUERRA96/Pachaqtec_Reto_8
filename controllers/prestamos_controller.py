from classes.personas import Persona
from classes.persona_rol import Persona_rol
from classes.prestamos  import Prestamos
from controllers.libros_controller import Libro_controller
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Prestamo_controller:
    def __init__(self):
        self.persona = Persona()
        self.persona_rol = Persona_rol()
        self.libro_controlador = Libro_controller()
        self.prestamo = Prestamos()

    def solicitar_libro(self):
        pass
    
    def revisar_solicitudes(self):
        pass

    def seguimiento_libros(self):
        pass

    def historial_solicitudes_lector(self):
        pass
