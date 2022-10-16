from deportista import Deportista
from persona import Persona


class Futbolista:
    _listaFutbolistas = list()

    def __init__(self, golesMarcados, tarjetasRojas, piernaHabil, nombre, edad, altura, sexo, deporte, anosPracticando) -> None:
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, deporte, anosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista._listaFutbolistas.append(self)

        def __str__(self):
            return f"Mi nombre es {self.getNombre()} soy profesional en el deporte {self.getDeporte()} Tengo {self.getEdad()} años de edad y llevo {self.getAñosPracticando()} años en el deporte"

        def setNombre(self, golesMarcados):
            self._golesMarcados = golesMarcados

        def getNombre(self):
            return self._golesMarcados

        def setNombre(self, tarjetasRojas):
            self._tarjetasRojas = tarjetasRojas

        def getNombre(self):
            return self._tarjetasRojas