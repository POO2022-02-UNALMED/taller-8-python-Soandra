class Deportista:
    def __init__(self, deporte, anosPracticando):
        self._deporte = deporte
        self._anosPracticando = anosPracticando

    def setNombre(self, deporte):
        self._deporte = deporte

    def getNombre(self):
        return self._deporte

    def setNombre(self, anosPracticando):
        self._anosPracticando = anosPracticando

    def getNombre(self):
        return self._anosPracticando