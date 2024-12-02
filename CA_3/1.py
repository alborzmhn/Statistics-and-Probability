from keras.datasets import mnist
import tensorflow as tf
import numpy as np, random
import matplotlib.pyplot as plt
from scipy import stats
from math import sqrt

def set_seed(seed):
  np.random.seed(seed)
  random.seed(seed)
set_seed(863458534)

(_, _) , (test_images, _) = mnist.load_data()
test_images = test_images.reshape(test_images.shape[0] , -1)
test_images = test_images.astype('float32') / 255.0

autoencoder = tf.keras.models.load_model('mnist_AE.h5')
reconstructed_images = autoencoder.predict(test_images)

for i in range(4):
    rand_int = random.randint(0, 10000)
    test = np.reshape(test_images[rand_int], (28,28))
    reconstructed = np.reshape(reconstructed_images[rand_int], (28,28))
    plt.imshow(test)
    plt.show()
    plt.imshow(reconstructed)
    plt.show()



def calculate_MSE(test_images, reconstructed_images):
    MSE = []
    for i in range(10000):
        err = test_images[i] - reconstructed_images[i]
        error_sum = np.sum(err * err)
        MSE.append(error_sum / (28 * 28))
    return MSE
MSE = []
MSE = calculate_MSE(test_images, reconstructed_images)
plt.hist(MSE)
plt.show()



def calculate_mean(MSE):
    temp_mean = 0
    for data in MSE:
        temp_mean += data
    mean = temp_mean / len(MSE)
    return mean
def calculate_enheraf_meyar(MSE, mean):
    temp_variance = 0
    for data in MSE:
        temp_variance += ((data - mean) ** 2)
    variance = temp_variance / len(MSE)
    enheraf_meyar = sqrt(temp_variance) 
    return enheraf_meyar

sample = np.random.choice(MSE, 1000)
mean = calculate_mean(sample)
enheraf_meyar = calculate_enheraf_meyar(sample, mean)
ks_statistic, p_value = stats.kstest(sample, cdf='norm', args= (mean, enheraf_meyar))
print(p_value)