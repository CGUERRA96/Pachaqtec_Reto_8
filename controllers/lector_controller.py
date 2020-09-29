from classes.personas import Persona
from controllers.libros_controller import Libro_controller
from controllers.prestamos_controller import Prestamo_controller
from controllers.administrador_controller import Administrador_controller
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Lector_controller:
    def __init__(self):
        self.persona = Persona()        
        self.libro_controlador = Libro_controller()
        self.administrador_controller = Administrador_controller()
        self.prestamo_controlador = Prestamo_controller()

    def menu(self):
        print('''
        ========================
            Bienvenido Lector
        ========================
        ''')
        self.identificar_lector()
        while True:
            try:
                print()
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
        self.administrador_controller.listar_lectores()

        id_lector = input_data("Ingrese el ID del profesor >> ", "int")
        lector = self.persona.obtener_persona({'id_persona': id_lector})
        #print(print_table(lector, ['id_persona', 'dni_persona', 'nombres', 'apellidos', 'correo', 'telefono', 'direccion', 'id_tipo_rol']))

        print(f'''
            ==============================================
                Bienvenido Lector : {lector[2]} {lector[3]}
            ==============================================
        ''')
    
