from scipy.io import wavfile
import matplotlib.pyplot as plt
from graph_widget import GraphWidget
import numpy as np
from plotting_function import RT60, find_nearest_value

RANGE_DICT = {"Low": 250, "Mid": 1000, "High": 4000}


class ReverbFormModel(GraphWidget):
    def __init__(self):
        super().__init__("Reverb")

    def plot_waveform(self, ranges, add_graph=False):
        sample_rate, data = wavfile.read("file.wav")
        spectrum, freqs, t, im = plt.specgram(data, Fs=sample_rate, NFFT=1024, cmap=plt.get_cmap('autumn_r'))

        reverb_creator = RT60(RANGE_DICT[ranges], spectrum, freqs, t, im)

        data_in_db = reverb_creator.frequency_check()
        index_of_max = np.argmax(data_in_db)
        value_of_max = data_in_db[index_of_max]
        sliced_array = data_in_db[index_of_max:]

        value_of_max_less_5 = value_of_max - 5
        value_of_max_less_5 = find_nearest_value(sliced_array, value_of_max_less_5)
        index_of_max_less_5 = np.where(data_in_db == value_of_max_less_5)

        value_of_max_less_25 = value_of_max - 25
        value_of_max_less_25 = find_nearest_value(sliced_array, value_of_max_less_25)
        index_of_max_less_25 = np.where(data_in_db == value_of_max_less_25)

        rt20 = (reverb_creator.time[index_of_max_less_5] - reverb_creator.time[index_of_max_less_25])[0]
        rt60 = 3 * rt20

        if not add_graph:
            self.new_plot_xy(reverb_creator.time, data_in_db)
        else:
            self.add_plot(reverb_creator.time, data_in_db)

    def plot_all(self):
        self.subplot.cla()
        for key in RANGE_DICT:
            self.plot_waveform(key, True)
