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
                menu = ['Mostrar Categorías', 'Ingresar Categoría', 'Buscar Categoría', "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_categorias()
                elif respuesta == 2:
                    self.insertar_categoria()
                elif respuesta == 3:

                    #self.listar_categorias()

                    #id_categoria = input_data("Ingrese el ID de la categoria a modificar >> ", "int")

                    self.buscar_categoria()
                    
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_categorias(self):
        try:
            print('''
            ===========================
                Lista de Categorías
            ===========================
            ''')
            libro = self.categoria.obtener_categorias('id_categoria')
            print(print_table(libro, ['ID', 'Categoria de Libro']))
            input("\nPresione una tecla para continuar...")
        except Exception as e:
            print(f'Oops! occurred {str(e)}')
           

    def insertar_categoria(self):
        descripcion = input_data("Ingrese la nueva categoría >> ")
        self.categoria.guardar_categoria({
            'descripcion': descripcion
        })
        print('''
        =================================
            Nueva Categoría Agregada !
        =================================
        ''')
        self.listar_categorias()

    def buscar_categoria(self):
        print('''
        ===========================
            Buscar Categoria
        ===========================
        ''')
        try:
            self.listar_categorias()
            id_categoria = input_data("Ingrese el ID de la categoria >> ", "int")
            categoria = self.categoria.obtener_categoria({'id_categoria': id_categoria})
            print(print_table(categoria, ['ID', 'Nombre']))

            if categoria:
                if pregunta("¿Deseas dar mantenimiento al curso?"):
                    opciones = ['Editar Categoría', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_categoria(id_categoria)
        except Exception as e:
            print(f'{str(e)}')
        input("\nPresione una tecla para continuar...")

    def editar_categoria(self, id_categoria):
        self.listar_categorias()
        id_categoria = input_data("Ingrese el ID de la categoria a modificar >> ", "int")
        descripcion = input_data("Ingrese la nueva categoria >> ")
        self.categoria.modificar_categoria({
            'id_categoria': id_categoria
        }, {
            'descripcion': descripcion
        })
        print('''
        ===========================
            Categoria Editada !
        ===========================
        ''')