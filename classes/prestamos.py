from connection.conn import Conexion

class Prestamos:
    def __init__(self):
        self.model = Conexion('prestamo')

    def guardar_prestamo(self, prestamo):
        return self.model.insert(prestamo)

    def obtener_prestamo(self, id_prestamo):
        return self.model.get_by_id(id_prestamo)

    def obtener_stock_prestado_libro(self, dataw, grupo):
        return self.model.get_by_column_group(dataw, grupo)

    def obtener_prestamos(self, order):
        return self.model.get_all(order)

    def buscar_prestamos(self, data_prestamo):
        return self.model.get_by_column(data_prestamo)

    def modificar_prestamo(self, id_prestamo, data_prestamo):
        return self.model.update(id_prestamo, data_prestamo)

    def eliminar_prestamo(self, id_periodo):
        return self.model.delete(id_periodo)
