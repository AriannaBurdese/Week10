from database.DAO import DAO
import networkx as nx
from geopy.distance import geodesic



class Model:
    def __init__(self):
        self._lista_fermate= []
        self._dizionario_fermate = {}
        self._grafo = None

    def getAllFermate(self):
        fermate = DAO.readAllFermate()
        self._lista_fermate = fermate
        #mi sono costruito un dizionario di fermate con chiave: id fermata
        # e valore l'oggetto fermata corrispondente
        for fermata in self._lista_fermate:
            self._dizionario_fermate[fermata.id_fermata] = fermata

    def creaGrafo(self):
        self._grafo = nx.MultiDiGraph() # DiGraph grafo ORIENTATO, MultiGraph più archi tra 2 nodi, MultiDiGraph multi grafo orientato
        print(len(self._lista_fermate))
        for fermata in self._lista_fermate:
            self._grafo.add_node(fermata)

        #primo modo di aggiungere gli archi, con 619*619 query sql
            """"
        for u in self._grafo: #per ognuno dei 619 nodi
            for v in self._grafo: #per ognuno dei possibili nodi connessi
                risultato = DAO.existsConnessioneTra(u, v) #chiedo al dao se esiste una connessione tra u e v
                if(len(risultato) > 0): # c e almeno un arco
                    self._grafo.add_edge(u, v) #creo arco
                    print(f"Aggiunto arco tra {u} e {v}")"""


        #secondo modo, con 619 query a cercare i nodi vicini
        """
        conta = 0
        for u in self._grafo:
            connessioniAvicini = DAO.searchViciniAFermata(u)
            for connessione in connessioniAvicini:
                fermataArrivo = self._dizionario_fermate[connessione.id_stazA]
                self._grafo.add_edge(u,fermataArrivo)
                print(f"Aggiunto arco tra {u} e {fermataArrivo}")
                print(len(self._grafo.edges()))
        print(self._grafo)"""

        #terzo modo, con una query sola che estrae in un colpo solo tutte le conn
        """
        lista_connessioni = DAO.readALLConnessioni()
        for c in lista_connessioni:
            u_nodo = self._dizionario_fermate[c.id_stazP]
            v_nodo = self._dizionario_fermate[c.id_stazA]
            self._grafo.add_edge(u_nodo,v_nodo)
            print(f"Aggiunto arco tra {u_nodo} e {v_nodo}")
            
        print(self._grafo)"""
        """
        #COSTRUISCO UN GRAFO PESATO
        lista_connessioni = DAO.readAllConnessioni()
        for c in lista_connessioni:
            u_nodo = self._dizionario_fermate[c.id_stazP]
            v_nodo = self._dizionario_fermate[c.id_stazA]

            # se ho gia arco incremento numero archi, altrimenti lo creo
            if self._grafo.has_edge(u_nodo, v_nodo): #uso la funzione di networkx per controllare se ho gia l'arco
                self._grafo[u_nodo][v_nodo]["peso"] += 1
            else:
                self._grafo.add_edge(u_nodo, v_nodo, peso=1)
            print(f"Aggiunto arco tra {u_nodo} e {v_nodo}, peso: {self._grafo[u_nodo][v_nodo]['peso']}")
            """

        #print(self._grafo)
        #COSTRUISCO UN MULTIGRAFO NEL QUALE IL PESO DEGLI ARCHI è IL TEMPO DI PERCORRENZA
        lista_connessioni = DAO.readAllConnessioni()
        for c in lista_connessioni:
            u_nodo = self._dizionario_fermate[c.id_stazP]
            v_nodo = self._dizionario_fermate[c.id_stazA]

            punto_u = (u_nodo.coordX, u_nodo.coordY)
            punto_v = (v_nodo.coordX, v_nodo.coordY)
            distanza = geodesic(punto_u, punto_v).km

            velocita = DAO.readVelocita(c._id_linea)
            print(f"Distanza: {distanza}, Velocita: {velocita}")
            tempo_perc = distanza / velocita * 60 #tempo percorrenza in minuti
            self._grafo.add_edge(u_nodo, v_nodo, tempo = tempo_perc)
            print(f"Aggiunto arco tra {u_nodo} e {v_nodo}, tempo: {tempo_perc}")

        #print(self._grafo)









