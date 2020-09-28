from connection.conn import Conexion

class Persona_rol:
    def __init__(self):
        self.model = Conexion('persona_rol')

    def guardar_persona_rol(self, persona_rol):
        return self.model.insert(persona_rol)

    def obtener_persona_rol(self, id_prol):
        return self.model.get_by_id(id_prol)

    def obtener_personas_rol(self, order):
        return self.model.get_all(order)

    def buscar_personas_rol(self, data_pers_rol):
        return self.model.get_by_column(data_pers_rol)

    def modificar_personas_rol(self, id_prol, data_pers_rol):
        return self.model.update(id_prol, data_pers_rol)

    def eliminar_persona_rol(self, id_prol):
        return self.model.delete(id_prol)
