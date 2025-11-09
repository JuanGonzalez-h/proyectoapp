class Amigo:

    def __init__(self, nombre, cumpleanos, gustos, recuerdo):
        self.nombre = nombre
        self.cumpleanos = cumpleanos
        self.gustos = gustos
        self.recuerdos = recuerdo

    def obtenerNombre(self):
        return self.nombre
    
    def obtenerCumpleanos(self):
        return self.nombre
    
    def agregarRecuerdo(self, nuevo_recuerdo):
        self.recuerdos.append(nuevo_recuerdo)
        return "Recuerdo agregado: " + nuevo_recuerdo
    
    def obtenerInfo(self):
        return "Nombre: " + self.nombre
    
    def generarNotificacion(self):
        return "Notificacion para " + self.nombre