from classes.personas import Persona
from controllers.libros_controller import Libro_controller
from controllers.prestamos_controller import Prestamo_controller
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Administrador_controller:
    def __init__(self):
        self.persona = Persona()        
        self.libro_controlador = Libro_controller()
        self.prestamo_controlador = Prestamo_controller()

    def menu(self):
        while True:
            try:
                print('''
                =============================
                   Bienvenido Administrador
                =============================
                ''')
                self.identificar_administrador()
                menu = ['Mostrar Administradores', "Mostrar Lectores", 'Inscribir personas', "Revisar solicitudes de préstamo", "Seguimiento de libros prestados", "Mantenimiento de estados de préstamos", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_administradores()
                elif respuesta == 2:
                    self.listar_lectores()
                elif respuesta == 3:
                    self.inscribir_personas()
                elif respuesta == 4:
                    self.prestamo_controlador.revisar_solicitudes()
                elif respuesta == 5:
                    self.prestamo_controlador.seguimiento_libros()
                elif respuesta == 6:
                    pass
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def identificar_administrador(self):
        #buscas y seleccionas un administrador (filtro N° 1 en tipo_rol)
        pass

    def listar_administradores(self):
        #Buscar administradores (filtro administrador rol)
        pass

    def listar_lectores(self):
        #Buscar lectores (filtro lector rol)
        pass

    def inscribir_personas(self):
        #Ingresa persona y coloca su rol (1: Administrador y 2: Lector)
        pass

