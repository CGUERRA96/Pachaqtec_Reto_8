from classes.personas import Persona
from controllers.libros_controller import Libro_controller
from controllers.prestamos_controller import Prestamo_controller
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Lector_controller:
    def __init__(self):
        self.persona = Persona()        
        self.libro_controlador = Libro_controller()
        self.prestamo_controlador = Prestamo_controller()

    def menu(self):
        while True:
            try:
                print('''
                ========================
                   Bienvenido Lector
                ========================
                ''')
                self.identificar_lector()
                menu = ['Buscar libros', "Solicitar libro", "Historial de solicitudes","Salir"]
                respuesta = Menu(menu).show()
                if respuesta == 1:
                    self.libro_controlador.listar_libros()
                elif respuesta == 2:
                    self.prestamo_controlador.solicitar_libro()
                elif respuesta == 3:
                    self.prestamo_controlador.historial_solicitudes_lector()          
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def identificar_lector(self):
        # Buscar e identificar al lector (filtro N° 2 en la tabla personas)
        pass
    
