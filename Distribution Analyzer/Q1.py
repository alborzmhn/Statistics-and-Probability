import numpy
from numpy import random
import matplotlib.pyplot as plt

trials = 500
samples = 5000
p_values = numpy.arange(0, 1.01, 0.01)
x = p_values

def sampleBin(m, n, probability):
    matrix = random.choice([0, 1], p = [1 - probability, probability], size = (m, n))
    return numpy.sum(matrix, axis=1)
    
def calculateTheoreticalExp():
    y = numpy.array([trials * p for p in p_values])
    plt.plot(x, y)

def calculatePracticalExp():
    y = numpy.array([numpy.sum(sampleBin(samples, trials, p)) / samples for p in p_values])
    plt.plot(x, y)
    
def calculateTheoreticalVar():
    y = numpy.array([trials * p * (1 - p) for p in p_values])
    plt.plot(x, y)
    
def calculatePracticalVar():
    y = numpy.array([numpy.var(sampleBin(samples, trials, p)) for p in p_values])
    plt.plot(x, y)
        
calculateTheoreticalExp()
calculatePracticalExp()
calculateTheoreticalVar()
calculatePracticalVar()
plt.show()