import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self, e):

        self.providerScelto= self._view._ddProvider.value
        soglia= self._view._txtInDistanza.value
        try:
            fsoglia= float(soglia)
        except ValueError:
            self._view._txt_result.controls.append(ft.Text("Inserire un valore numerico"))
        self._model.buildGraph(self.providerScelto, fsoglia)
        self._view._txt_result.controls.append(ft.Text(f"Grafo creato: Vertici: {self._model.getNumNodi()} e num archi {self._model.getNumArchi()}"))
        self.fillDDTarget()
        self._view.update_page()


    def handleAnalizzaGrafo(self, e):
        parziale, max=self._model.getMaxVicini()
        self._view._txt_result.controls.append(ft.Text("Vertici con piu vicini"))
        for n in parziale:
            self._view._txt_result.controls.append(ft.Text(f"{n}  vicini={max}"))

        self._view.update_page()

    def handleCalcolaPercorso(self, e):
        self._view._txt_result.clean()
        stringa= self._view._txtInString.value
        if stringa == "":
            self._view._txt_result.controls.append(ft.Text("Inserire una stringa"))
            self._view.update_page()
            return

        target=self._view._ddTarget.value

        self._model.searchPath(target, stringa)
        soluzione= self._model.getBestSoluzione()
        self._view._txt_result.controls.append(ft.Text(f"Soluzione più luga:"))

        for n in soluzione:
            self._view._txt_result.controls.append(ft.Text(f" {n}"))

        self._view.update_page()






    def fillDDProvider(self):
        provider=self._model.getProvider()
        for prov in provider:
            self._view._ddProvider.options.append(ft.dropdown.Option(prov))

    def fillDDTarget(self):
        locations = self._model.getAllLocations()

        for loc in locations:
            self._view._ddTarget.options.append(ft.dropdown.Option(loc))



    def readChoiceLocation(self, e):
        if e.control.data is None:
            self._choiceLocation = None
        else:
            self._choiceLocation = e.control.data
