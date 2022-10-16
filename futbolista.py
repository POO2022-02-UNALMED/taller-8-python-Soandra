from deportista import Deportista
from persona import Persona


class Futbolista:
    _listaFutbolistas = list()

    def __init__(self, golesMarcados, tarjetasRojas, piernaHabil, nombre, edad, altura, sexo, añosPracticando, deporte = "Futbol"):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, deporte, añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)

        def __str__(self):
            return f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"

        def setGolesMarcados(self, golesMarcados):
            self._golesMarcados = golesMarcados

        def getGolesMarcados(self):
            return self._golesMarcados

        def setTarjetasRojas(self, tarjetasRojas):
            self._tarjetasRojas = tarjetasRojas

        def getTarjetasRojas(self):
            return self._tarjetasRojas

        def setPiernaHabil(self, piernaHabil):
            self._piernaHabil = piernaHabil

        def getPiernaHabil(self):
            return self._piernaHabil