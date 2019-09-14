from functools import reduce
import tensorflow as tf


def digit_choose(l):
    @staticmethod
    def merge(a, b):
        if a[1] > b[1]:
            a
        else:
            b
    return map(lambda d, _: d, reduce(merge, enumerate(l)))


def fix_gpu():
    # Fix: see https://github.com/tensorflow/tensorflow/issues/24496
    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    for device in physical_devices:
        tf.config.experimental.set_memory_growth(device, True)
