import numpy as np
from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print ('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap

def curve_calcu(point, para, type):
    if type == "parabola":
        y = ((point - para[0][0]) ** 2) / (4 * para[1]) + para[0][1]
        return y
    if type == "linear":
        y = point * para[0] + para[1]
        return y


def curve_maker(start, peak, type):
    if type == "parabola":
        c = (((start[0] - peak[0]) ** 2) / (start[1] - peak[1])) / 4
        return [peak, c]
    elif type == "linear":
        b = (peak[1] - start[1]) / (peak[0] - start[0])
        c = start[1] - b * start[0]
        return [b, c]


def smooth_interval_scale(start_iv, end_iv, num_iv, peak_scale, peak_iv, type):
    '''

    :param start_iv: 200
    :param end_iv: 600
    :param num_iv: 10    number of inttervals between 200 and 600
    :param peak_scale: 10
    :param peak_iv: 5     index of  the interval under 200 Hz as 0
    :param type:  "parabola",  "linear"
    :return: nparray, nparray
    '''
    interval = np.arange(start_iv, end_iv + (end_iv - start_iv) / num_iv, (end_iv - start_iv) / num_iv)
    para_front = curve_maker([0,1], [peak_iv, peak_scale], type)
    para_back = curve_maker([num_iv+1,1], [peak_iv, peak_scale], type)
    scales = []

    for idx in range(num_iv+2):
        if idx<=peak_iv:
            scales.append(curve_calcu(idx, para_front, type))
        else:
            scales.append(curve_calcu(idx, para_back, type))

    # scales.append(1)  # head and tail(original bands) intervals are 1

    return interval, np.array(scales)
