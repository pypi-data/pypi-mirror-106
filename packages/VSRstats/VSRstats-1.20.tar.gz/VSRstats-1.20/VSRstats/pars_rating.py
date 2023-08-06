import numpy as np
from collections import Counter
from peakutils import peak
from struct import unpack
import math
import os

import pyhrv.time_domain as td
from pyhrv import tools
from scipy import stats
from VSRstats.time_domain import time_domain
from VSRstats import getPeaks

class pars_rating:
    
    def __init__(self, data):

        if type(data) == list:
            data = np.array(data)
        if type(data) == np.ndarray:
            self.stats = (self._computeSignal(data) if
                           data.ndim == 1 else self._computeSignals(data))
        else:
            raise TypeError('Signal should be an np.ndarray')

    def _computeSignals(self, signals):
        return np.array([self.computeSignal(s) for s in signals])

    def _firstParam(self, peaks):
        peaks_diff = tools.nni_diff(peaks)
        
        # First Parametr        
        M = np.mean(peaks_diff) * 10
        
        if (M <= 660):
            return 2
        elif (M <= 800):
            return 1
        elif (M >= 1000):
            return -1
        elif (M >= 1200):
            return -2
        return 0

    def _secoundParam(self, sdnn, vr, cv):
        if (sdnn <= 20 and vr <= .1 and cv <= 2):
            return 2
        elif (sdnn >= 100 and vr >= .3 and cv >= 8):
            return 1
        elif (vr >= .1 and vr <= .3):
            return 0
        elif (sdnn >= 100 and vr >= .45 and cv >= 8):
            return -1
        elif (vr >= .6):
            return -2
        return 0

    def _computeSignal(self, signal):
        obj = {}
        parsCount = 0
        
        stats = time_domain(signal).stats

        peaks = getPeaks(signal)
        parsCount += self._firstParam(peaks)
        
        sdnn_ms = stats['sdnn'] * 10;
        cv_m = stats['cv'] / sdnn_ms
        
        #parsCount += self._secoundParam(sdnn_mc, )
        
        return parsCount
