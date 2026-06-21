from model.model import Model

model = Model()
model.getAllFermate()
model.creaGrafo() #mi dice quanti nodi e quanti archi ho, se nel model scrivo print(self._grafo)
print(model._lista_fermate)

for nodo in model._grafo.nodes():
    print(f"{nodo}, grado: {model._grafo.out_degree[nodo]}")


