import numpy as np


class RT60:
    def __init__(self, freqs, ranges):
        self.freqs = freqs
        self.ranges = ranges

    def range_finder(self):
        for x in self.freqs:
            if x > self.ranges:
                break
        return x

    def frequency_check(self, spectrum):
        target_frequency = self.freqs.range_finder(self.ranges)
        index_of_frequency = np.where(self.freqs == target_frequency)[0][0]
        data_for_frequency = spectrum[index_of_frequency]

        data_in_db_fun = 10 * np.log10(data_for_frequency)
        return data_in_db_fun
