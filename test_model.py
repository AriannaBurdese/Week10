from model.model import Model

model = Model()
model.getAllFermate()
model.creaGrafo()
print(model._lista_fermate)

for nodo in model._grafo.nodes():
    print(f"{nodo}, grado: {model._grafo.out_degree[nodo]}")


