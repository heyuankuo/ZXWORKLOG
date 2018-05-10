import tensorflow as tf
import numpy as np

a = np.loadtxt('odom.txt') 
x_data = a[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise
print (x_data)