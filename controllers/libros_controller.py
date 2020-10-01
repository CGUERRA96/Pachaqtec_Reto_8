from classes.categoria import Categoria
from classes.libros import Libro
from classes.prestamos import Prestamos
from controllers.categoria_controller import Categoria_controller
from helpers.helper import input_data, print_table, pregunta
from helpers.menu import Menu
from datetime import datetime


class Libro_controller:
    def __init__(self):
        self.categoria = Categoria()
        self.libro = Libro()
        self.prestamo = Prestamos()
        self.categoria_controlador = Categoria_controller()
        
    def menu(self):
        while True:
            try:
                print('''
                =============================
                   Mantenimiento de Libros
                =============================
                ''')
                menu = ['Mostrar libros', 'Ingresar libro', 'Buscar libro', "Mantenimiento Categoría libro", "Salir"]
                respuesta = Menu(menu).show()
                
                if respuesta == 1:
                    self.listar_libros()
                elif respuesta == 2:
                    self.insertar_libro()
                elif respuesta == 3:
                    self.buscar_libros_filtros()
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

        print(print_table(libro, ['ID', 'Libro','Autor','Categoria','Editorial','Año de edición','Stock']))
        input("\nPresione una tecla para continuar...")

    def insertar_libro(self):
        nombre_libro = input_data("Ingrese el nombre del libro >> ")
        
        autor = input_data("Ingrese el nombre del autor del libro >> ")
        
        self.categoria_controlador.listar_categorias()
        
        id_categoria = input_data("Ingrese el código de la categoría >> ")
        
        editorial = input_data("Ingrese el nombre de la editorial del libro >> ")
        

        while True:

            anio_edicion = input_data("Ingrese el año de edición del libro >> ",'int')

            ahora = datetime.now()
            anio = ahora.year

            if anio_edicion >= 1000 and anio_edicion <= anio:
                #anio_edicion = input_data("Ingrese el año de edición del libro >> ")
                break
            else:
                print('Ingresar el año correcto del libro.')

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


    def buscar_libro(self):

        print('''
        ======================
            Buscar Libros
        ======================
        ''')
        try:
            self.listar_libros()

            id_libro = input_data("Ingrese el ID del libro >> ")
            libros = self.libro.buscar_libros({'id_libro' : id_libro})
            print(print_table(libros,['ID', 'Libro','Autor','Categoria','Editorial','Año de edición','Stock']))

            if libros:
                if pregunta(f"¿Deseas dar mantenimiento al libro?"):
                    opciones = ['Editar libro', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.editar_libro(id_libro)
        except Exception as e:
            print(f'{str(e)}')


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
            libros_buscados = self.libro.buscar_libros_like(libros_buscar)
            print(print_table(libros_buscados,['ID', 'Libro','Autor','Categoria','Editorial','Año de edición','Stock']))

            if libros_buscados:
                if pregunta(f"¿Deseas dar mantenimiento al libro?"):
                    opciones = ['Editar libro', 'Salir']
                    respuesta = Menu(opciones).show()
                    if respuesta == 1:
                        self.listar_libros()
                        id_libro = input_data("Ingrese el ID del libro >> ")
                        self.editar_libro(id_libro)

    def buscar_libros_filtros_lector(self):
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
            libros_buscados = self.libro.buscar_libros_like(libros_buscar)
            print(print_table(libros_buscados,['ID', 'Libro','Autor','Categoria','Editorial','Año de edición','Stock']))


    def editar_libro(self, id_libro):
        #buscas el libro y editas
        #self.listar_libros()
        nombre_libro = input_data("Ingrese el nombre del libro >> ")
        autor = input_data("Ingrese el nombre del autor a modificar >> ")
        self.categoria_controlador.listar_categorias()
        id_categoria = input_data("Ingrese el código a modificar >> ")
        editorial = input_data("Ingrese el nombre de la editorial del libro a modificar >> ")
        anio_edicion = input_data("Ingrese el año de edición del libro a modificar >> ")
        stock_libro = input_data("Ingrese la cantidad de libros a modificar >> ")
        self.libro.modificar_libros({
            'id_libro': id_libro
        }, {
            'nombre': nombre_libro,
            'autor': autor,
            'id_categoria': id_categoria,
            'editorial': editorial,
            'anio_edicion' : anio_edicion,
            'stock_libro' : stock_libro
        })
        print('''
        ========================
            Libro Editado !
        ========================
        ''')

