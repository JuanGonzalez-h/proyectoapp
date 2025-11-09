from ManipuladorTexto import ManipuladorTexto

class ManipuladorTextoPersonalizado(ManipuladorTexto):
    
    def _init_(self, estiloFormal):
        ManipuladorTexto._init_(self)
        self.estiloFormal = estiloFormal
    
    def manipuladoTexto(self, texto):
        
        if self.estiloFormal:
           return texto
        else:
         return texto
    
    def formatearNotificacion(self, amigo):
        nombre = amigo.obtenerNombre()
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
