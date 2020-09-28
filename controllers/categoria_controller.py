from classes.categoria import Categoria
from classes.libros import Libro
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Categoria_controller:
    def __init__(self):
        self.categoria = Categoria()
        self.libro = Libro()
        
    def menu(self):
        while True:
            try:
                print('''
                ===============================
                   Mantenimiento de Categoria
                ===============================
                ''')
                menu = ['Mostrar Categorías', 'Ingresar Categoría', 'Editar Categoría', "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_Categorias()
                elif respuesta == 2:
                    self.insertar_categoria()
                elif respuesta == 3:
                    self.editar_categoria()               
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_Categorias(self):
        print('''
        ===========================
            Lista de Categorías
        ===========================
        ''')
        libro = self.categoria.obtener_categorias('id_categoria')
        print(print_table(libro, ['ID', 'Categoria de Libro']))
        input("\nPresione una tecla para continuar...")

    def insertar_categoria(self):
        pass

    def editar_categoria(self):
        pass