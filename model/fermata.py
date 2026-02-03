from dataclasses import dataclass


@dataclass
class Fermata:
    _id_fermata: int #private
    _nome : str
    _coordX: float
    _coordY: float
    @property #metodo getter
    def id_fermata(self): # -> int:
        return self._id_fermata
    @property
    def nome(self): # -> str:
        return self._nome
    @property
    def coordX(self):
        return self._coordX
    @property
    def coordY(self):
        return self._coordY

    def __str__(self):
        return f"Fermata: {self._id_fermata} {self._nome} {self._coordX} {self._coordY}"

    def __hash__(self): #restiuisce hash della chiave, mi assicura fermata univoca
        return hash(self._id_fermata)

