from scipy.io import wavfile
from graph_model import GraphWidget


class WaveformModel(GraphWidget):
    def __init__(self):
        super().__init__("Waveform")

    def plot_waveform(self):
        self.subplot.clear()
        samplerate, data = wavfile.read("file.wav")
        self.new_plot_arr(data)
