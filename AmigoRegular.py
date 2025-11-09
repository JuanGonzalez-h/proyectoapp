from Amigo import Amigo
class AmigoRegular(Amigo):
    
    def _init_(self,nombre, cumpleanos, gustos, recuerdo, anecdotas):
      super().init_(nombre, cumpleanos, gustos, recuerdo)
      self.anecdotas = anecdotas 

    def agregarRecuerdo(self, nuevo_recuerdo):
       recuerdo_formateado = "[Regular]" + nuevo_recuerdo
       self.recuerdo.apped(recuerdo_formateado)
       return "Recuerdo regular agregado:" + nuevo_recuerdo
    
    def obtenerInfo(self):
        info = "=== AMIGO REGULAR ===\n"
        info = info + "Nombre: " + self.nombre + "\n"
        info = info + "Cumpleaños: " + self.cumpleanos + "\n"

        gustos_texto = ""
        for i in range(len(self.gustos)):
           gustos_texto = gustos_texto + self.gustos[i]
           if i < len(self.gustos) - 1:
              gustos_texto = gustos_texto + ","
            
        info = info + "Gustos: " + gustos_texto + "\n"
        info = info + "Anecdotas: " + str(len(self.anecdotas))
        return info
    
    def generarNotificacion(self):
        return "📢 Recordatorio: Contactar a " + self.nombre + " (Amigo Regular) "