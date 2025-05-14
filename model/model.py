import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._products = DAO.getProducts()

    def buildGraph(self,color,year):
        self._graph = nx.Graph
        self._graph.add_nodes_from(self._products)
        allEdges = DAO.getEdges(,)