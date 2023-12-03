from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure


class GraphWidget(FigureCanvas):
    def __init__(self, x, y):
        super().__init__(Figure())
        subplot = self.figure.subplots()
        self.figure.set_facecolor((.26, .33, .52))
        subplot.set_facecolor((.26, .33, .52))
        subplot.plot(x, y, "k")
        subplot.spines['bottom'].set_color((.961, .910, .780))
        subplot.spines['top'].set_color((.961, .910, .780))
        subplot.spines['left'].set_color((.961, .910, .780))
        subplot.spines['right'].set_color((.961, .910, .780))
        subplot.xaxis.label.set_color((.961, .910, .780))
        subplot.tick_params(axis='x', colors=(.961, .910, .780))
        subplot.yaxis.label.set_color((.961, .910, .780))
        subplot.tick_params(axis='y', colors=(.961, .910, .780))
