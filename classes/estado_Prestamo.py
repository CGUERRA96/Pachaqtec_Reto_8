from connection.conn import Conexion

class Estado_prestamo:
    def __init__(self):
        self.model = Conexion('estado_prestamo')

    def guardar_estado_prestamo(self, estado_prestamo):
        return self.model.insert(estado_prestamo)

    def obtener_estado_prestamo(self, id_estado):
        return self.model.get_by_id(id_estado)

    def obtener_estados_prestamo(self, order):
        return self.model.get_all(order)

    def buscar_estados_prestamo(self, data_estado):
        return self.model.get_by_column(data_estado)

    def modificar_estado_prestamo(self, id_libro, data_estado):
        return self.model.update(id_libro, data_estado)

    def eliminar_estado_prestamo(self, id_estado):
        return self.model.delete(id_estado)