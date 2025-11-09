from Amigo import Amigo

class AmigoCercano(Amigo):

    def __init__(self, nombre, cumpleanos, gustos, recuerdo, anecdotas, nivelConfianza):
        super().__init__(nombre, cumpleanos, gustos, recuerdo)
        self.anecdotas = anecdotas
        self.nivelConfianza = nivelConfianza

    def agregarRecuerdo(self, nuevo_recuerdo):
        recuerdo_especial = "[Cercano] " + nuevo_recuerdo
        self.recuerdo.append(recuerdo_especial)
        return "Recuerdo especial agregado: " + nuevo_recuerdo
    
    def obtenerInfo(self):
        info = "== AMIGO CERCANO ===\n"
        info = info + "Nombre: " + self.nombre + "\n"
        info = info + "Cumpleaños: " + self.cumpleanos + "\n"

        gustos_texto = ""
        for i in range(len(self.gustos)):
            gustos_texto = gustos_texto + self.gustos[i]
            if i < len(self.gustos) - 1:
                gustos_texto = gustos_texto + ", "
        
        info = info + "Gustos: " + gustos_texto + "\n"
        info = info + "Nivel de Confianza: " + str(self.nivelConfianza) + "/10\n"
        info = info + "Anécdotas: " + str(len(self.anecdotas))
        return info
    
    def generarNotificacion(self):
        return "💙 Importante: Recordar contactar a " + self.nombre + " (Amigo Cercano)"
    
    def compararMomento(self):
        cantidad = str(len(self.recuerdo))
        return "Momentos compartidos con " + self.nombre + ": " + cantidad