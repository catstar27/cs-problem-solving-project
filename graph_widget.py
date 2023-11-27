from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure


class GraphWidget(FigureCanvas):
    def __init__(self, x, y):
        super().__init__(Figure())
        subplot = self.figure.subplots()
        self.figure.set_facecolor("black")
        subplot.set_facecolor("black")
        subplot.plot(x, y)
        subplot.spines['bottom'].set_color('red')
        subplot.spines['top'].set_color('red')
        subplot.spines['left'].set_color('red')
        subplot.spines['right'].set_color('red')
        subplot.xaxis.label.set_color('red')
        subplot.tick_params(axis='x', colors='red')
        subplot.yaxis.label.set_color('red')
        subplot.tick_params(axis='y', colors='red')
