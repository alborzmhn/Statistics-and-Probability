import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score 

def create_list(a, b):
  result = []
  for i in range(len(a)):
    result.append(a[i] * b[i])
  return result
def calculate_slope(n, sumx, sumy, sumxx, sumxy):
  return (n * sumxy - (sumx * sumy)) / (n * sumxx - (sumx ** 2))
def calculate_intercept(slope, sumy, sumx, n):
  return (sumy - slope * sumx) / n
def calculate_r2(n, sumx, sumy, sumxx, sumyy, sumxy):
  temp1 = n * sumxy - (sumx * sumy)
  temp2 = (n * sumxx - (sumx ** 2)) ** 0.5
  temp3 = (n * sumyy - (sumy ** 2)) ** 0.5
  return (temp1 / (temp2 * temp3)) ** 2
def regression(x, y):
  n = len(x)
  xx = create_list(x, x)
  yy = create_list(y, y)
  xy = create_list(x, y)
  sumx = sum(x)
  sumy = sum(y)
  sumxx = sum(xx)
  sumyy = sum(yy)
  sumxy = sum(xy)
  a = calculate_slope(n, sumx, sumy, sumxx, sumxy)
  b = calculate_intercept(a, sumy, sumx, n)
  r2 = calculate_r2(n, sumx, sumy, sumxx, sumyy, sumxy)
  fig, ax = plt.subplots()
  ax.axline((0, b), slope = a)
  ax.plot(x, y, 'ro')
  ax.set_title(f'R2 value : {r2}')
  plt.show()
  print(r2)

x = [-2.3, -1.1, 0.5, 3.2, 4.0, 6.7, 10.3, 11.5]
y = [-9.6, -4.9, -4.1, 2.7, 5.9, 10.8, 18.9, 20.5]
regression(x, y)
#with outlier point
regression(x + [5.8], y + [31.3])
#with high leverage point
regression(x + [20.4], y + [14.1])
#with outlier high leverage point
regression(x + [20.4], y + [31.3])
