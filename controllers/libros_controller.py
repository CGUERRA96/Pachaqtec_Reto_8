from classes.categoria import Categoria
from classes.libros import Libro
from controllers.categoria_controller import Categoria_controller
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu

class Libro_controller:
    def __init__(self):
        self.categoria = Categoria()
        self.libro = Libro()
        self.categoria_controlador = Categoria_controller()
        
    def menu(self):
        while True:
            try:
                print('''
                =============================
                   Mantenimiento de Libros
                =============================
                ''')
                menu = ['Mostrar libros', 'Ingresar libro', 'Editar libro', "Mantenimiento Categoría libro", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_libros()
                elif respuesta == 2:
                    self.insertar_libro()
                elif respuesta == 3:
                    self.editar_libro()
                elif respuesta == 4:
                    self.categoria_controlador.menu()
                else:
                    self.salir = True
                    break
            except Exception as e:
                print(f'{str(e)}')

    def listar_libros(self):
        # Tener en cuenta que stock debe ser calculado restado de la cantidad préstamos para ese libro en estado 'aprobado'
        print('''
        ========================
            Lista de Libros
        ========================
        ''')
        libro = self.libro.obtener_libros('id_libro')
        print(print_table(libro, ['ID', 'Libro','Autor','Categoria','Editorial','Año de edición','Stock']))
        input("\nPresione una tecla para continuar...")

    def insertar_libro(self):
        nombre_libro = input_data("Ingrese el nombre del libro >> ")
        autor = input_data("Ingrese el nombre del autor del libro >> ")
        self.categoria_controlador.listar_Categorias()
        id_categoria = input_data("Ingrese el código de la categoría >> ")
        editorial = input_data("Ingrese el nombre de la editorial del libro >> ")
        anio_edicion = input_data("Ingrese el año de edición del libro >> ")
        stock_libro = input_data("Ingrese la cantidad de libros >> ")
        # si no existe libro agregar pero si existe debe sumarse el stock
        self.libro.guardar_libro({
            'nombre': nombre_libro,
            'autor': autor,
            'id_categoria': id_categoria,
            'editorial': editorial,
            'anio_edicion' : anio_edicion,
            'stock_libro' : stock_libro
        })
        print('''
        ==============================
            Nuevo Libro agregado !
        ==============================
        ''')
        self.listar_libros()

    def editar_libro(self):
        #buscas el libro y editas
        pass


