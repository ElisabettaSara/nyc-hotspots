import copy
import random

import networkx as nx

from database.DAO import DAO
from geopy.distance import distance



class Model:
    def __init__(self):
        self._grafo= nx.Graph()
        self.archiD=[]
        self.bestSol=[]


    def searchPath(self,vf, stringa):
        sources = self.archiD
        source = sources[random.randint(0, len(sources) - 1)]
        self.sotStr= stringa
        self.finale=vf
        self.distanzaMax=0
        print("ciao sono qui")

        parziale=[source]
        pesi=[0]
        archi_visitati=[]
        self.ricorsione(parziale, archi_visitati)
        print(self.bestSol)

    def ricorsione(self, parziale, archi_visitati):
        last=parziale[-1]
        vicini = self._grafo[last]

        vicini_utilizzabili = []
        for v in vicini:
            if (last,v) not in archi_visitati and (v, last) not in archi_visitati and self.sotStr not in v:
                vicini_utilizzabili.append(v)

        if (len(vicini_utilizzabili)==0 and parziale[-1]==self.finale) or parziale[-1]==self.finale:
            if len(parziale)> self.distanzaMax:
                self.distanzaMax = len(parziale)
                self.bestSol=copy.deepcopy(parziale)

            return

        for v in vicini_utilizzabili:
            archi_visitati.append((last, v))
            parziale.append(v)

            self.ricorsione(parziale, archi_visitati)

            archi_visitati.pop()
            parziale.pop()


    def getBestSoluzione(self):
        return self.bestSol







    def getProvider(self):
        provider = DAO.getProvider()
        #print(provider)
        provider.sort()

        return provider

    def buildGraph(self, provider, soglia):

        self._grafo.clear()
        nodi = DAO.getNodes(provider)
        #print(len(nodi))

        self._grafo.add_nodes_from(nodi)

        tutto= DAO.getAll(provider)
        #distanza += distance.geodesic((v1.Lat, v1.Lng), (v2.Lat, v2.Lng)).km
        for t in tutto:

            self.distanza = distance((t[1],t[2]),(t[-2],t[-1])).km
            #print(t[2],t[3],t[-2],t[-1])
            if self.distanza<=soglia:

                self._grafo.add_edge(t[0],t[3],weight=self.distanza)

    def getMaxVicini(self):
        max=0
        parziale=[]
        self.archiD=[]

        for nodi in self._grafo.nodes():
            if len(self._grafo[nodi])> max:
                max = len(self._grafo[nodi])
        for nodi in self._grafo.nodes():
            if len(self._grafo[nodi])==max:
                parziale.append(nodi)
                self.archiD.append(nodi)
        return parziale,max

    def getNumNodi(self):
        return (len(self._grafo.nodes))

    def getNumArchi(self):
        return(len(self._grafo.edges))

    def getAllLocations(self):
        return self._grafo.nodes





