from connection.conn import Conexion

class Alumno:
    def __init__(self):
        self.model = Conexion('administrador')

    def guardar_administrador(self, administrador):
        return self.model.insert(administrador)

    def obtener_administrador(self, id_administrador):
        return self.model.get_by_id(id_administrador)

    def obtener_administradores(self, order):
        return self.model.get_all(order)

    def buscar_administradores(self, data_administrador):
        return self.model.get_by_column(data_administrador)

    def modificar_administrador(self, id_administrador, data_administrador):
        return self.model.update(id_administrador, data_administrador)

    def eliminar_administrador(self, id_administrador):
        return self.model.delete(id_administrador)
