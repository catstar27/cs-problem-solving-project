import numpy as np
import scipy.signal as signal
import math


def my_resample(x, newnum, y):
    method = 0

    if (0 == method):
        if (len(y) != len(x)):
            print("my_resample: Error: lengths of x and y are not equal!")
        # pad signal such that its length is a power of 2 = much faster
        orig_len = len(x)
        p2_len = int(math.pow(2, math.ceil(math.log(orig_len) / math.log(2))))
        x3 = np.zeros(p2_len)
        y3 = np.zeros(p2_len)
        x3[0:orig_len - 1] = x[0:orig_len - 1]
        y3[0:orig_len - 1] = y[0:orig_len - 1]
        x2, y2 = signal.resample(x3, newnum * p2_len // orig_len, y3)
        x2 = x2[0:newnum - 1]
        y2 = y2[0:newnum - 1]
    else:
        newnum = int(newnum)
        num = len(x)
        stride = int(num / newnum)
        x2 = np.zeros(newnum)
        y2 = np.zeros(newnum)
        i = 0
        for i2 in range(0, newnum):
            i = i2 * stride
            x2[i2] = x[i]
            y2[i2] = y[i]
    return x2, y2

class RT60:
    def update_graph(self, amp, t):
        """Updates the graph with new data/annotations"""

        if len(amp) <= 1: return  # do nothing when there's nothing to graph

        epsilon = 1.0e-8  # added to avoid log(0) errors

        # Compute the quantity to be plotted
        power = (amp + epsilon) ** 2
        maxval = 1.0 * np.max(power)
        power = power / maxval
        dB = 10 * np.ma.log10(np.abs(power))  # "ma"=masked array, throws out -Inf values

        # Downsample for plotting purposes.  (otherwise the plotting takes forever)
        nsamples = len(dB)
        if (nsamples > 100000):
            plotsamples = 2048
        elif (nsamples > 50000):
            plotsamples = 2048
        else:
            plotsamples = 1024
        ds_dB, ds_t = my_resample(dB, plotsamples, t)

        return ds_dB, ds_t
