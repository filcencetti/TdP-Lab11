import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._products = DAO.getProducts()
        self._graph = None
        self._idMap = {}
        for v in self._products:
            self._idMap[v.Product_number] = v

    def buildGraph(self,year,color):
        self._graph = nx.Graph()
        for prod in self._products:
            if prod.Product_color == color:
                self._graph.add_node(prod)
        allEdges = DAO.getEdges(year,color)
        for edge in allEdges:
            self._graph.add_edge(self._idMap[edge[0]], self._idMap[edge[1]], weight=edge[2])

    def searchPath(self,code):
        self._max_edge = 0
        lun_percorso = 0
        for arch in list(self._graph.edges(self._idMap[code],data=True)):
            self.path = []
            self.recursive_path(arch)
            if len(self.path) > lun_percorso:
                lun_percorso = len(self.path)

        return lun_percorso

    def recursive_path(self, arch):
            for u, v, weight in self._graph.edges(arch[1],data=True):
                if (u,v,weight) not in self.path and weight["weight"] >= self._max_edge:
                    self._max_edge = weight["weight"]
                    self.path.append((u, v, weight))
                    self.recursive_path((u,v,weight))
                    self.path.pop()