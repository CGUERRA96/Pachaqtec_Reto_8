from helpers.menu import Menu
import pprint
from controllers.lector_controller import Lector_controller
from controllers.libros_controller import Libro_controller
from controllers.administrador_controller import Administrador_controller

def iniciar_app():
    try:
        print('''
        =============================
            Sistema Bibliotecario
        =============================
        ''')
        menu_principal = ["Administrador", "Lector", "Libros", "Salir"]
        respuesta = Menu(menu_principal).show()
        if respuesta == 1:
            
            administrador = Administrador_controller()
            administrador.menu()
            if administrador.salir:
                iniciar_app()

        elif respuesta == 2:
            
            lector = Lector_controller()
            lector.menu()
            if lector.salir:
                iniciar_app()

        elif respuesta == 3:
            
            libros = Libro_controller()
            libros.menu()
            if libros.salir:
                iniciar_app()

        print("\nGracias por utilizar el sistema\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

iniciar_app()