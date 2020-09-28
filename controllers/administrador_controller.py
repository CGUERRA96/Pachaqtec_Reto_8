from classes.personas import Persona
from classes.persona_rol import Persona_rol
from controllers.libros_controller import Libro_controller
from controllers.prestamos_controller import Prestamo_controller
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Administrador_controller:
    def __init__(self):
        self.persona = Persona()
        self.persona_rol = Persona_rol()
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
                menu = ['Mostrar Administradores', "Mostrar Lectores", 'Inscribir personas', "Revisar solicitudes", "Seguimiento de libros prestados", "Salir"]
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
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def identificar_administrador(self):
        #buscas y seleccionas un administrador
        pass

    def listar_administradores(self):
        #Buscar administradores (filtro administrador rol)
        pass

    def listar_lectores(self):
        #Buscar lectores (filtro lector rol)
        pass

    def inscribir_personas(self):
        #Ingresa persona y luego su rol (dos tablas que ingresar)
        pass

