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
                menu = ['Mostrar Estados', 'Ingresar Estados', 'Editar Estados', "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_estados()
                elif respuesta == 2:
                    self.insertar_estado()
                elif respuesta == 3:
                    self.editar_estado()               
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

    def insertar_estado(self):
        pass

    def editar_estado(self):
        pass