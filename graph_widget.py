from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class GraphWidget(FigureCanvasQTAgg):
    """
    Widget for use in the main GUI containing a graph with x and y specified by the constructor.
    """
    def __init__(self, title):
        super().__init__(Figure())
        self.title = title
        self.subplot = self.figure.subplots()
        self.subplot.title.set_text(self.title)

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

    def new_plot_xy(self, x, y):
        self.subplot.cla()
        self.subplot.plot(x, y, "k")
        self.subplot.title.set_text(self.title)
        self.draw()

    def new_plot_arr(self, arr):
        self.subplot.cla()
        self.subplot.plot(arr, "k")
        self.subplot.title.set_text(self.title)
        self.draw()
