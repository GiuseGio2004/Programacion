from Color import Color

class Borde:
    def __init__(self, grosor: int, color: 'Color'):
        """Constructor de la clase Borde que recibe el grosor y el color."""
        self.grosor = grosor
        self.color = color
    
    def obtenerGrosor(self) -> int:
        """Devuelve el grosor del borde."""
        return self.grosor
    
    def obtenerColor(self) -> 'Color':
        """Devuelve el color del borde."""
        return self.color
    
    def copiarValores(self, borde: 'Borde'):
        """Copia los valores de otro borde."""
        self.grosor = borde.obtenerGrosor()
        self.color = borde.obtenerColor()  # Suponiendo que la clase Color es inmutable o tiene su propia forma de copiar.
    
    def clonar(self) -> 'Borde':
        """Retorna un clon superficial de este borde."""
        # Retorna una nueva instancia con los mismos atributos (grosor y color).
        return Borde(self.grosor, self.color)
    
    def esIgualQue(self, borde: 'Borde') -> bool:
        """Verifica si este borde es igual a otro borde."""
        return self.grosor == borde.obtenerGrosor() and self.color == borde.obtenerColor()
    
    def __str__(self):
        """Devuelve una representación en cadena del borde."""
        return f"Borde: Grosor={self.grosor}, Color={self.color}"