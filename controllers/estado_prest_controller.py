from classes.estado_prestamo import Estado_prestamo
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Estado_prestamo_controller:
    def __init__(self):
        self.estado_prestamo = Estado_prestamo()
        
    def menu(self):
        while True:
            try:
                print('''
                ===============================
                   Mantenimiento de Estados
                ===============================
                ''')
                menu = ['Mostrar Estados', 'Ingresar Estados', 'Buscar Estados', "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_estados()
                elif respuesta == 2:
                    self.insertar_estado()
                elif respuesta == 3:
                    self.buscar_estado()               
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_estados(self):
        print('''
        ===========================
            Lista de Estados
        ===========================
        ''')
        estados_prestamo = self.estado_prestamo.obtener_estados_prestamo('id_estado')
        print(print_table(estados_prestamo, ['ID', 'Nombre estado']))
        input("\nPresione una tecla para continuar...")
    
    def buscar_estado(self):
        print('''
        ==============================
            Buscar estado prestamo
        ==============================
        ''')
        try:
            self.listar_estados()
            id_estado = input_data("Ingrese el ID del estado prestamo >> ", "int")
            estado = self.estado_prestamo.obtener_estado_prestamo({'id_estado': id_estado})
            print(print_table(estado, ['ID', 'Nombre']))

            if estado:
                if pregunta("¿Deseas dar mantenimiento al estado?"):
                    opciones = ['Editar estado', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_estado(id_estado)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def insertar_estado(self):
        nombre_estado = input_data("Ingrese el estado del libro >> ")
        self.estado_prestamo.guardar_estado_prestamo({
            'nombre_estado': nombre_estado,            
        })
        print('''
        ================================
            Estado prestamo agregado
        ================================
        ''')
        self.listar_estados()

    def editar_estado(self, id_estado):
        nombre_estado = input_data("Ingrese estado del libro >> ")         
        self.estado_prestamo.modificar_estado_prestamo({
            'id_estado': id_estado
        }, {
            'nombre_estado': nombre_estado,
        })
        print('''
        ===============================
            Estado prestamo editado
        ===============================
        ''')
    
    def eliminar_estado(self, id_estado):
        self.estado_prestamo.eliminar_estado_prestamo({
            'id_estado': id_estado
        })
        print('''
        =================================
            Estado prestamo eliminado
        =================================
        ''')