import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self,e):
        self._model.creaGrafo()
    

    def handleCercaRaggiungibili(self,e):
        pass

    def populate_dropdown(self,dd):  #deve ricevere una dropdown
        self._model.getAllFermate() #vado a prendere tutte le fermate dal Model, che si prende dal Dao
        # le fermate le trovo nel model, in _lista_fermate

        for fermata in self._model._lista_fermate:
            dd.options.append(ft.dropdown.Option(key = fermata.id_fermata, #qui specifico cosa voglio come chiave, l'id che viene passato quando seleziono fermata dal dropdown
                                                 text = fermata.nome)) #voglio avere una chiave e poi mostrare un testo nella dd

