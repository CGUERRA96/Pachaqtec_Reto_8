from helpers.menu import Menu
import pprint

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
            
            pass

        elif respuesta == 2:
            
            pass

        elif respuesta == 3:
            
            pass

        print("\nGracias por utilizar el sistema\n")
    except KeyboardInterrupt:
        print('\n Se interrumpio la aplicación')
    except Exception as e:
        print(f'{str(e)}')

iniciar_app()