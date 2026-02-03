from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.fermata import Fermata


class DAO():
    pass
    @staticmethod
    def readAllFermate():
        conn = DBConnect.get_connection()
        result = []
        query = ("SELECT * FROM Fermata")
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            fermata = Fermata(row["id_fermata"], row["nome"], row["coordX"], row["coordY"])
            result.append(fermata)
            print(row)
        cursor.close()
        conn.close()
        return result #restituisco lista di oggetti Fermata DTO
    @staticmethod
    def existsConnessioneTra(u : Fermata,v : Fermata): #scrivendo u:Fermata dico a Pycharm che u e v sono delle fermate
        #verifica se esista una connessione tra nodo u e v
        conn = DBConnect.get_connection()
        result = []
        query = ("""SELECT * 
                 FROM connessione c
                 where c.id_stazP = %s AND c.id_stazA = %s
                 """)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (u.id_fermata, v.id_fermata ) ) #parametro con ( , )
        for row in cursor:
            connessione = Connessione(row["id_connessione"],
                                      row["id_linea"],
                                      row["id_stazP"],
                                      row["id_stazA"])
            result.append(row)

            print(row)
        cursor.close()
        conn.close()
        return result


    def searchViciniAFermata(u : Fermata,v): #scrivendo u:Fermata dico a Pycharm che u e v sono delle fermate
        #cerco le fermate collegate a quella passata come parametro
        conn = DBConnect.get_connection()
        result = []
        query = ("""SELECT * 
                 FROM connessione c
                 where c.id_stazP = %s
                 """)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (u.id_fermata, ) ) #parametro con (,)
        for row in cursor:
            connessione = Connessione(row["id_connessione"],
                                      row["id_linea"],
                                      row["id_stazP"],
                                      row["id_stazA"])
            result.append(connessione)

            print(row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def readAllConnessioni(): #scrivendo u:Fermata dico a Pycharm che u e v sono delle fermate
        #cerco le fermate collegate a quella passata come parametro
        conn = DBConnect.get_connection()
        result = []
        query = ("""SELECT * 
                 FROM connessione c
                 """)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query ) #non passo nessun parametro
        for row in cursor:
            connessione = Connessione(row["id_connessione"],
                                      row["id_linea"],
                                      row["id_stazP"],
                                      row["id_stazA"])
            result.append(connessione)

            print(row)
        cursor.close()
        conn.close()
        return result







    def readVelocita(id_linea):
        conn = DBConnect.get_connection()
        result = []
        query = ("SELECT  * FROM linea where id_linea = %s")
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query, (id_linea, ))
        for row in cursor:
            result.append(row["velocita"])
        cursor.close()
        conn.close()
        return result[0] #la prima riga contiene la velocità letta
