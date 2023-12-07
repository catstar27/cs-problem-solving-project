import numpy as np

class RT60:
    def __init__(self, ranges, spectrum, freqs, time, im):
        self.ranges = ranges
        self.spectrum = spectrum
        self.freqs = freqs
        self.time = time
        self.im = im
    def range_finder(self):
        for x in self.freqs:
            if x > self.ranges:
                break
        return x
    def frequency_check(self):
        target_frequency = self.freqs.range_finder(self.ranges)
        index_of_frequency = np.where(self.freqs == target_frequency)[0][0]
        data_for_frequency = self.spectrum[index_of_frequency]

        data_in_db_fun = 10 * np.log10(data_for_frequency)
        return data_in_db_fun
    def update_range(self, new_freqs):
        self.freqs = new_freqs
def find_nearest_value(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]


