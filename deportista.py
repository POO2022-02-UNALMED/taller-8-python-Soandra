class Deportista:
    def __init__(self, deporte, añosPracticando):
        self._deporte = deporte
        self._añosPracticando = añosPracticando

    def setDeporte(self, deporte):
        self._deporte = deporte

    def getDeporte(self):
        return self._deporte

    def setAnosPracticando(self, añosPracticando):
        self._añosPracticando = añosPracticando

    def getAnosPracticando(self):
        return self._añosPracticando