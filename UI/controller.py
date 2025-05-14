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
        for c in colors:
            self._view._ddcolor.options.append(ft.dropdown.Option(c))

    def handle_graph(self, e):
        self._model.buildGraph(self._view._ddyear.value,self._view._ddcolor.value.Product_color)


    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
