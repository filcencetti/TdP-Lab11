import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        for i in [2015, 2016, 2017, 2018]:
            self._view._ddyear.options.append(ft.dropdown.Option(i))

        colors = set()
        for product in self._model._products:
            colors.add(product.Product_color)
        for c in sorted(list(colors)):
            self._view._ddcolor.options.append(ft.dropdown.Option(c))

    def handle_graph(self, e):
        self._view.txtOut.controls.clear()
        self._view._ddnode.options.clear()
        self._view.txtOut2.controls.clear()
        self._view.update_page()
        self._model.buildGraph(self._view._ddyear.value,self._view._ddcolor.value)
        self._view.txtOut.controls.append(ft.Text(f"Il grafo ha {self._model._graph.number_of_nodes()} nodi e {self._model._graph.number_of_edges()} archi"))
        top_3 = self.printTOP3()
        self._view.txtOut.controls.append(ft.Text(f"I nodi ripetuti sono: {top_3}"))
        self.fillDDProduct()
        self._view.update_page()

    def fillDDProduct(self):
        for node in self._model._graph.nodes():
            self._view._ddnode.options.append(ft.dropdown.Option(f"{node.Product_number}"))


    def handle_search(self, e):
        self._view.txtOut2.controls.clear()
        self._view.txtOut2.controls.append(ft.Text(f"Numero archi percorso più lungo da {self._view._ddnode.value} : {self._model.searchPath(int(self._view._ddnode.value))}"))
        self._view.update_page()

    def printTOP3(self):
        edges = []
        top_3 = []
        for edge in sorted(list(self._model._graph.edges(data=True)), key=lambda ed: ed[2]["weight"],reverse=True):
            self._view.txtOut.controls.append(ft.Text(f"Arco da {edge[0]} a {edge[1]}, peso = {edge[2]["weight"]}"))
            edges.append(edge[0])
            edges.append(edge[1])
            if len(edges) == 6:
                conteggi = {}
                for elem in edges:
                    if elem in conteggi:
                        conteggi[elem] += 1
                    else:
                        conteggi[elem] = 1

                for elem, count in conteggi.items():
                    if count > 1:
                        top_3.append(elem.Product_number)

                return top_3