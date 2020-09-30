from classes.personas import Persona
from controllers.libros_controller import Libro_controller
from controllers.prestamos_controller import Prestamo_controller
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu
from controllers.estado_prest_controller import Estado_prestamo_controller

class Administrador_controller:
    def __init__(self):
        self.persona = Persona()        
        self.libro_controlador = Libro_controller()
        self.prestamo_controlador = Prestamo_controller()
        self.estado_prest_controller = Estado_prestamo_controller()

    def menu(self):
        print('''
        ================================
            Bienvenido Administrador
        ================================
        ''')
        self.identificar_administrador()
        while True:
            try:
                
                print()

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
                    self.estado_prest_controller.menu()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def identificar_administrador(self):
        #buscas y seleccionas un administrador (filtro N° 1 en tipo_rol)
        self.listar_administradores()

        id_admin = input_data("Ingrese el ID del profesor >> ", "int")
        admin = self.persona.obtener_persona({'id_persona': id_admin})
        #print(print_table(lector, ['id_persona', 'dni_persona', 'nombres', 'apellidos', 'correo', 'telefono', 'direccion', 'id_tipo_rol']))

        print(f'''
            ==================================================
                Bienvenido Administrador : {admin[2]} {admin[3]}
            ==================================================
        ''')
    
    def listar_personas(self):
        print('''
        =======================
        =  Lista de Personas  =
        =======================
        ''')
        #personas_adm = self.persona.obtener_personas('id_persona')
        persona = self.persona.obtener_personas('id_persona')
        print(print_table(persona, ['id_persona', 'dni_persona', 'nombres', 'apellidos', 'correo', 'telefono', 'direccion', 'id_tipo_rol']))
        input("\nPresione una tecla para continuar...")

    def listar_administradores(self):
        #Buscar administradores (filtro administrador rol)
        print('''
        ==============================
        =  Lista de Administradores  =
        ==============================
        ''')
        id_tipo_rol = 1
        personas_adm = self.persona.buscar_personas({'id_tipo_rol': id_tipo_rol})
        print(print_table(personas_adm, ['id_persona', 'dni_persona', 'nombres', 'apellidos', 'correo', 'telefono', 'direccion', 'id_tipo_rol']))
        input("\nPresione una tecla para continuar...")

    def listar_lectores(self):
        #Buscar lectores (filtro lector rol)
        print('''
        =======================
        =  Lista de Lectores  =
        =======================
        ''')
        id_tipo_rol = 2
        personas_lec = self.persona.buscar_personas({'id_tipo_rol': id_tipo_rol})
        print(print_table(personas_lec, ['id_persona', 'dni_persona', 'nombres', 'apellidos', 'correo', 'telefono', 'direccion', 'id_tipo_rol']))
        input("\nPresione una tecla para continuar...")

    def inscribir_personas(self):
        #Ingresa persona y coloca su rol (1: Administrador y 2: Lector)
        dni = input_data("Ingrese el nuevo DNI >> ")
        nombre = input_data("Ingrese el nuevo nombre >> ")
        apellidos = input_data("Ingrese el nuevo apellido >> ")
        correo = input_data("Ingrese el nuevo correo >> ")
        telefono = input_data("Ingrese el nuevo telefono >> ")
        direccion = input_data("Ingrese la nueva direccion >> ")
        id_tipo_rol = input_data("Ingrese el ID rol >> ", "int")
        self.persona.guardar_persona({
            'dni_persona ': dni,
            'nombres': nombre,
            'apellidos': apellidos,
            'correo': correo,
            'telefono': telefono,
            'direccion': direccion,
            'id_tipo_rol': id_tipo_rol
        })
        print('''
        ==========================
            Persona Agregada !
        ==========================
        ''')

        self.listar_personas()



