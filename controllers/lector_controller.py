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
        id_lector_1 = self.identificar_lector()
        id_lector_1
        if id_lector_1:
            while True:            
                try:
                    print()
                    menu = ['Buscar libros', "Solicitar libro", "Historial de solicitudes","Salir"]
                    respuesta = Menu(menu).show()
                    if respuesta == 1:
                        self.libro_controlador.buscar_libros_filtros_lector()
                    elif respuesta == 2:
                        self.prestamo_controlador.solicitar_libro(id_lector_1)
                    elif respuesta == 3:
                        self.prestamo_controlador.historial_solicitudes_lector(id_lector_1)          
                    else:
                        self.salir = True
                        break
                except Exception as e:
                    print(f'{str(e)}')
        
    def identificar_lector(self):
        # Buscar e identificar al lector (filtro N° 2 en la tabla personas)
        id_tipo_rol = 2
        lector_0 = self.persona.buscar_personas({'id_tipo_rol': id_tipo_rol})
        if lector_0:
            self.administrador_controller.listar_lectores()
            id_lector = input_data("Ingrese el ID del lector >> ", "int")
            lector = self.persona.obtener_persona({'id_persona': id_lector})
            #print(print_table(lector, ['id_persona', 'dni_persona', 'nombres', 'apellidos', 'correo', 'telefono', 'direccion', 'id_tipo_rol']))

            print(f'''
                ==================================================
                    Bienvenido Lector : {lector[2]} {lector[3]}
                ==================================================
            ''')
            return id_lector
        else:
            print(f'\n Por favor comunicate con el administrador para que creen tu usuario :')
            input("\nPresione una tecla para continuar...")

