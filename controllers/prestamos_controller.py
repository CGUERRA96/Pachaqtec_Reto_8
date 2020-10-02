from classes.personas import Persona
from classes.prestamos  import Prestamos
from classes.estado_prestamo import Estado_prestamo
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
        self.estado_prest = Estado_prestamo()
        self.libros = Libro()

    def solicitar_libro(self, id_lector_identificado):
        print('Primero busquemos el libro que vas a solicitar >>\n')
        while True:            
            self.libro_controlador.buscar_libros_filtros_lector()
            if pregunta(f"¿Encontraste el libro que buscabas?"):
                id_libro_seleccionado = input_data("Ingresa el ID del libro a solicitar >> ")
                stock_i=self.stock_prestado_libro(id_libro_seleccionado) # stock prestado
                stock_p=self.libro_controlador.stock_inicial_libro(id_libro_seleccionado) # stock inicial
                stock_disponible = stock_i - stock_p
                if stock_disponible:
                    now = datetime.now()
                    fecha_ahora = now.strftime("%d-%m-%y %H:%M")
                    self.prestamo.guardar_prestamo({
                        'id_lector'    :   id_lector_identificado,
                        'id_libro'  :   id_libro_seleccionado,
                        'fecha_solicitud' :   fecha_ahora,
                        'id_estado_prestamo' : 1
                    })
                    print('''
                    ==============================
                        Solicitud creada !!
                    ==============================
                    ''')
                presentar = self.prestamo.obtener_prestamos('id_lector')
                print(print_table(presentar,['ID', 'Id_Lector', 'Id_Libro', 'Fecha solicitud', 'Id_administrador', 'Fecha prestamo', 'Plazo', 'Fecha devolución', 'Id_estado']))
                break
            else:
                if pregunta(f"¿Desea volver a intentar una búsqueda?"):
                    print('Busquemos el libro que vas a solicitar >>\n')
                else:
                    input("\nPresione una tecla para continuar...")
                    break
                   
    def revisar_solicitudes(self, id_administrador):
        id_estadop = 1
        solicitud_prestamo = self.prestamo.buscar_prestamos({'id_estado_prestamo': id_estadop})
        print('''
                =============================================
                    Solicitudes pendientes de aprobación
                =============================================
        ''')
        print(print_table(solicitud_prestamo, ['ID', 'Id_Lector', 'Id_Libro', 'Fecha solicitud', 'Id_administrador', 'Fecha prestamo', 'Plazo', 'Fecha devolución', 'Id_estado']))
        id_prest_sol = input_data("Ingrese el ID de la solicitud a revisar >> ")
        solicitud = self.prestamo.obtener_prestamo({'id_prestamo' : id_prest_sol})
        print(print_table(solicitud,['ID', 'Id_Lector', 'Id_Libro', 'Fecha solicitud', 'Id_administrador', 'Fecha prestamo', 'Plazo', 'Fecha devolución', 'Id_estado']))
        if pregunta(f"¿Desea aprobar esta solicitud?"):
            self.aprobar_solicitud(id_prest_sol, id_administrador)
            print(f'''
                =========================================================
                    Solicitud aprobada con ID : {solicitud[0]}
                =========================================================
            ''')
        else:
            self.rechazar_solicitud(id_prest_sol, id_administrador)
            print(f'''
                =========================================================
                    Solicitud rechazada con ID: {solicitud[0]}
                =========================================================
            ''')
        
    def aprobar_solicitud(self, id_prestamo, id_administrador):
        hoy = datetime.now()
        fecha_prest = hoy.strftime("%d-%m-%y %H:%M")
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
        fecha_prest = hoy.strftime("%d-%m-%y %H:%M")
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
        fecha_devol = hoy.strftime("%d-%m-%y %H:%M")       
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

    def seguimiento_libros(self, id_administrador):
        id_estado_a = 2
        seguimiento_prestamo = self.prestamo.buscar_prestamos({'id_estado_prestamo': id_estado_a})
        print('''
                =============================================
                    Préstamos sin devolución
                =============================================
        ''')
        print(print_table(seguimiento_prestamo, ['ID', 'Id_Lector', 'Id_Libro', 'Fecha solicitud', 'Id_administrador', 'Fecha prestamo', 'Plazo', 'Fecha devolución', 'Id_estado']))
        id_prest_dev = input_data("Ingrese el ID del prestamo a devolver >> ")
        solicitud = self.prestamo.obtener_prestamo({'id_prestamo' : id_prest_dev})
        print(print_table(solicitud,['ID', 'Id_Lector', 'Id_Libro', 'Fecha solicitud', 'Id_administrador', 'Fecha prestamo', 'Plazo', 'Fecha devolución', 'Id_estado']))
        if pregunta(f"¿Desea cambiar al estado devuelto?"):
            self.devolver_prestamo(id_prest_dev, id_administrador)
            print(f'''
                =========================================================
                    Préstamo devuelto con ID : {solicitud[0]}
                =========================================================
            ''')
        else:
            input("\nNo se realizó ninguna acción. Presione una tecla para continuar...")

    def historial_solicitudes_lector(self, id_lector):
        print('''
        ================================
            Historial de solicitudes
        ================================
        ''')
        historial_impr = []
        historial_prest = self.prestamo.buscar_prestamos({'id_lector': id_lector})        
        if historial_prest:
            for v in historial_prest:
                id_prest = v[0]
                id_lect = v[1]
                id_lib = v[2]
                fecha_sol = v[3]
                id_estado = v[8]
                nomb_lec = self.persona.obtener_persona({
                    'id_persona': id_lect
                })
                if not nomb_lec:
                    nomb_lec = ''                
                nomb_lib = self.libros.obtener_libro({
                    'id_libro': id_lib
                })
                if not nomb_lib:
                    nomb_lib = ''
                nomb_estado = self.estado_prest.obtener_estado_prestamo({
                    'id_estado': id_estado
                })
                if not nomb_estado:
                    nomb_estado = ''
                historial_impr.append({
                        'ID': id_prest,
                        'Lector': nomb_lec[1] + " " + nomb_lec[2],
                        'Libro': nomb_lib[1],
                        'Fecha Solicitud': fecha_sol,
                        'Estado': nomb_estado[1]
                })
            print(print_table(historial_impr))

    def stock_prestado_libro(self, id_libro):
        id_estado_0 = 2     
        libro_stock_prestado = self.prestamo.obtener_stock_prestado_libro({'id_libro': id_libro,'id_estado_prestamo': id_estado_0},{'id_libro': id_libro})
        print(print_table(libro_stock_prestado,['ID Libro','Stock Prestado']))
        
        for z in libro_stock_prestado:
            stock_1 = z[1]
     
        print(stock_1)
        return stock_1
 
