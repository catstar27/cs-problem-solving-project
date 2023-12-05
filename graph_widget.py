from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure


class GraphWidget(FigureCanvas):
    """
    Widget for use in the main GUI containing a graph with x and y specified by the constructor.
    """
    def __init__(self):
        super().__init__(Figure())
        self.subplot = self.figure.subplots()

        # Color customization
        self.figure.set_facecolor((.26, .33, .52))
        self.subplot.set_facecolor((.26, .33, .52))
        self.subplot.spines['bottom'].set_color((.961, .910, .780))
        self.subplot.spines['top'].set_color((.961, .910, .780))
        self.subplot.spines['left'].set_color((.961, .910, .780))
        self.subplot.spines['right'].set_color((.961, .910, .780))
        self.subplot.xaxis.label.set_color((.961, .910, .780))
        self.subplot.tick_params(axis='x', colors=(.961, .910, .780))
        self.subplot.yaxis.label.set_color((.961, .910, .780))
        self.subplot.tick_params(axis='y', colors=(.961, .910, .780))

    def new_plot(self, x, y):
        self.subplot.plot(x, y, "k")
