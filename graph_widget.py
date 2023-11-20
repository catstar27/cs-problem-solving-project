from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure


class GraphWidget(FigureCanvas):
    def __init__(self, x, y):
        super().__init__(Figure())
        subplot = self.figure.subplots()
        subplot.plot(x, y)
