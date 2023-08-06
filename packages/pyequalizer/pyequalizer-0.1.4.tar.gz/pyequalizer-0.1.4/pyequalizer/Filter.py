import scipy
from scipy import signal
import numpy as np
from pyequalizer.utils import smooth_interval_scale, curve_maker, curve_calcu, timing

def band_filter(data, sr, min_frq, max_frq, step=3):
    Wn1 = 2*min_frq/sr
    Wn2 = 2*max_frq/sr
    b, a = signal.butter(step, [Wn1,Wn2], 'bandpass')   #配置滤波器 8 表示滤波器的阶数
    filtedData = signal.filtfilt(b, a, data)
    return filtedData

def high_filter(data, sr, min_frq, step=3):
    Wn1 = 2*min_frq/sr
    b, a = signal.butter(step, Wn1, 'highpass')   #配置滤波器 8 表示滤波器的阶数
    filtedData = signal.filtfilt(b, a, data)
    return filtedData

def low_filter(data, sr, max_frq, step=3):

    Wn1 = 2*max_frq/sr
    b, a = signal.butter(step, Wn1, 'lowpass')   #配置滤波器 8 表示滤波器的阶数
    filtedData = signal.filtfilt(b, a, data)
    return filtedData

def _equalizer(data, sr, interval, scales, step=3):
    '''data: double
        interval: seperation spots
        Ex: [200, 400, 600]

        scale: scale for each interval
        Ex:[0.5, 1, 1.5, 1]
        '''
    assert len(scales)-1 == len(interval)
    sum_y = np.zeros(data.shape[0])
    num_interval = len(interval)+1
    sum_y += low_filter(data, sr, interval[0],step = step)* scales[0]
    sum_y += high_filter(data, sr, interval[-1], step = step)*scales[-1]

    for i in range(num_interval-2):
        sum_y += band_filter(data, sr, interval[i], interval[i+1], step = step)*scales[i+1]

    return sum_y
# @timing
def equalizer(data, sr, start_iv, end_iv, num_iv, peak_scale, peak_iv, type, step=3):
    '''

    :param data:  nparray
    :param sr:  44100 (int)
    :param start_iv: 200 (double)
    :param end_iv: 600 (double)
    :param num_iv: 10    number of inttervals between 200 and 600 (int)
    :param peak_scale: 10 (int)
    :param peak_iv: 5     index of  the interval under 200 Hz as 0     (int)
    :param type:  "parabola",  "linear"
    :param step:  filter rank  (int)
    :return: nparray
    '''
    interval, scales = smooth_interval_scale(start_iv, end_iv, num_iv, peak_scale, peak_iv, type)
    data = _equalizer(data, sr, interval, scales, step=step)

    return data

