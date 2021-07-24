from keras.datasets import mnist 
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.utils import np_utils
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Conv2D, MaxPooling2D, Flatten
from keras.datasets import cifar10

(train_image, train_label), (test_image, test_label) = cifar10.load_data()
print(len(train_image))