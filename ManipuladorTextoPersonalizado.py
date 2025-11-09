from ManipuladorTexto import ManipuladorTexto

class ManipuladorTextoPersonalizado(ManipuladorTexto):
    
    def __init__(self, estiloFormal=True):
        super().__init__()
        self.estiloFormal = estiloFormal
    
def formatearNotificacion(self, amigo):
        nombre = amigo.nombre
        if self.estiloFormal:
            return "Estimado usuario, le recordamos contactar a: " + nombre
        else:
            return "Hey! No olvides hablar con " + nombre + " 😊"
    
def cambiarEstiloFormal(self, nuevo_estilo):
        self.estiloFormal = nuevo_estilo
        if nuevo_estilo:
            return "Estilo cambiado a: Formal"
        else:
            return "Estilo cambiado a: Informal"
        