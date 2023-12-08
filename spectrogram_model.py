from scipy.io import wavfile
from graph_model import GraphWidget
import matplotlib.pyplot as plt


class SpectrogramModel(GraphWidget):
    """
    Graphs the spectrogram of the wav
    """
    def __init__(self):
        super().__init__("Spectrogram")

    def plot_spectrogram(self):
        self.subplot.clear()
        self.subplot.title.set_text(self.title)
        samplerate, data = wavfile.read("file.wav")
        self.subplot.specgram(data, Fs=samplerate, mode="psd")
        self.draw()
