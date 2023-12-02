import numpy as np

class RT60():
    def measure(self, h, fs=1, decay_db=60, rt60_tgt=None):
        h = np.array(h)
        fs = float(fs)

        # The power of the impulse response in dB
        power = h ** 2
        energy = np.cumsum(power[::-1])[::-1]  # Integration according to Schroeder

        # remove the possibly all zero tail
        i_nz = np.max(np.where(energy > 0)[0])
        energy = energy[:i_nz]
        energy_db = 10 * np.log10(energy)
        energy_db -= energy_db[0]

        # -5 dB headroom
        i_5db = np.min(np.where(-5 - energy_db > 0)[0])
        e_5db = energy_db[i_5db]
        t_5db = i_5db / fs

        # after decay
        i_decay = np.min(np.where(-5 - decay_db - energy_db > 0)[0])
        t_decay = i_decay / fs

        # compute the decay time
        decay_time = t_decay - t_5db
        est_rt60 = (60 / decay_db) * decay_time

        return est_rt60
