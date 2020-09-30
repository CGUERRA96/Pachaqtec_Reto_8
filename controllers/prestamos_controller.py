from classes.personas import Persona
from classes.prestamos  import Prestamos
from classes.libros import Libro
from controllers.libros_controller import Libro_controller
from helpers.helper import input_data, print_table, pregunta
from datetime import datetime
from helpers.menu import Menu

class Prestamo_controller:
    def __init__(self):
        self.persona = Persona()
        self.libro_controlador = Libro_controller()
        self.prestamo = Prestamos()
        self.libros = Libro()

    def solicitar_libro(self, id_lector_identificado):
        print('Primero busquemos el libro que vas a solicitar >>\n')
        while True:            
            self.buscar_libros_filtros()
            if pregunta(f"¿Encontraste el libro que buscabas?"):
                id_libro_seleccionado = input_data("Ingresa el ID del libro a solicitar >> ")
                now = datetime.now()
                fecha_ahora = now.strftime("%Y-%m-%d %H:%M")
                self.prestamo.guardar_prestamo({
                    'id_lector'    :   id_lector_identificado,
                    'id_libro'  :   id_libro_seleccionado,
                    'fecha_solicitud' :   fecha_ahora
                })
                print('''
                ==============================
                    Solicitud creada !!
                ==============================
                ''')
                break
            else:
                if pregunta(f"¿Desea volver a intentar una búsqueda?"):
                    print('Busquemos el libro que vas a solicitar >>\n')
                else:
                    input("\nPresione una tecla para continuar...")
                    break
                   
    def revisar_solicitudes(self):
        id_estadop = 1
        solicitud_prestamo = self.prestamo.buscar_prestamos({'id_estado_prestamo': id_estadop})
        print('''
                =============================================
                    Solicitudes pendientes de aprobación
                =============================================
        ''')
        print(print_table(solicitud_prestamo, ['ID', 'Id_Lector', 'Id_Libro', 'Fecha solicitud', 'Id_administrador', 'Fecha prestamo', 'Plazo', 'Fecha devolución', 'Id_estado']))

    def aprobar_solicitud(self, id_prestamo, id_administrador):
        hoy = datetime.now()
        fecha_prest = hoy.strftime("%Y-%m-%d %H:%M")
        self.prestamo.modificar_prestamo({
                'id_prestamo': id_prestamo
            }, {
                'id_administrador': id_administrador,
                'fecha_prestamo': fecha_prest,
                'id_estado_prestamo': 2                  
            })
        print('''
            ========================
                Solicitud Aprobada !
            ========================
        ''')

    def rechazar_solicitud(self, id_prestamo, id_administrador):
        hoy = datetime.now()
        fecha_prest = hoy.strftime("%Y-%m-%d %H:%M")
        self.prestamo.modificar_prestamo({
                'id_prestamo': id_prestamo
            }, {
                'id_administrador': id_administrador,
                'fecha_prestamo': fecha_prest,
                'id_estado_prestamo': 3                  
            })
        print('''
            ========================
                Solicitud Rechazada !
            ========================
        ''')

    def devolver_prestamo(self, id_prestamo, id_administrador):
        hoy = datetime.now()
        fecha_devol = hoy.strftime("%Y-%m-%d %H:%M")       
        self.prestamo.modificar_prestamo({
                'id_prestamo': id_prestamo
            }, {
                'id_administrador': id_administrador,
                'id_estado_prestamo': 4,
                'fecha_devolucion': fecha_devol
                
            })
        print('''
            ========================
                Libro devuelto !
            ========================
        ''')

    def seguimiento_libros(self):
        id_estado_a = 2
        seguimiento_prestamo = self.prestamo.buscar_prestamos({'id_estado_prestamo': id_estado_a})
        print('''


                =============================================
                    Solicitudes aprobadas en seguimiento
                =============================================
        ''')
        print(print_table(seguimiento_prestamo, ['ID', 'Id_Lector', 'Id_Libro', 'Fecha solicitud', 'Id_administrador', 'Fecha prestamo', 'Plazo', 'Fecha devolución', 'Id_estado']))


    def historial_solicitudes_lector(self):
        pass

    def buscar_libros_filtros(self):
        #libros_1 = self.libros.obtener_libros('id_libro')
        libros_buscar = {}
       
        if pregunta(f"¿Deseas buscar por nombre de libro?"):
            nombre_libro_0 = input_data("Ingresa el nombre del libro: >> ")
            libros_buscar['nombre'] = nombre_libro_0

        if pregunta(f"¿Deseas buscar por nombre de autor?"):
            nombre_autor_0 = input_data("Ingresa el nombre del autor: >> ")
            libros_buscar['autor'] = nombre_autor_0

        if pregunta(f"¿Deseas buscar por Editorial?"):
            nombre_editorial_0 = input_data("Ingresa el nombre de la Editorial: >> ")
            libros_buscar['editorial'] = nombre_editorial_0
        libros_buscados = self.libros.buscar_libros_like(libros_buscar)
        print(print_table(libros_buscados,['ID','Nombre libro','Autor','Id_Categoria','Editorial','Año de edición','Stock']))