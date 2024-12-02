import pandas as pd
import numpy as np, random
import matplotlib.pyplot as plt
import math
import statsmodels.api as sm
import scipy.stats as stats

def set_seed(seed):
    np.random.seed(seed)
    random.seed(seed)
set_seed(854654403)
df = pd.read_csv('FIFA2020.csv', encoding = "ISO-8859-1")

#1
#print(df['dribbling'])
pace_mean, dribbling_mean = df[['pace', 'dribbling']].mean(numeric_only = True)
df['dribbling'] = df['dribbling'].fillna(dribbling_mean)
df['pace'] = df['pace'].fillna(pace_mean)
#print(df['dribbling'])

#2
box = df.boxplot(column = 'age')
box.plot()
plt.show()
min_data = df['age'].min()
max_data = df['age'].max()
q1 = df['age'].quantile(0.25)
q2 = df['age'].quantile(0.5)
q3 = df['age'].quantile(0.75)
print(min_data, max_data, q1, q2, q3)

#3
size1 = 100
size2 = 500
size3 = 2000

#3_a
def calculate_mean(x):
  mean = 0
  for num in x:
    mean += num
  mean /= len(x)
  return mean

def calculate_variance(x, mean):
  variance = 0
  for num in x:
    variance += (num - mean) ** 2
  variance /= len(x)
  return variance

def calculate_enheraf_meyar(variance):
  return (math.sqrt(variance))
   
def weight(size):
    weight = df['weight'].to_numpy()
    sample = np.random.choice(weight, size)
    mean = calculate_mean(sample)
    variance = calculate_variance(sample, mean)
    enheraf_meyar = calculate_enheraf_meyar(variance)
    print("for size : ", size, ",mean :", mean, ",variance :", variance, ",std :", enheraf_meyar)
    normal = np.random.normal(mean, enheraf_meyar, size3)
    sm.qqplot(sample, loc = mean, scale = enheraf_meyar, line = '45')
    statistic, p_value = stats.shapiro(sample)
    plt.title(f'n: {size}')
    plt.show()

weight(100)
weight(500)
weight(2000)


poisson_sample = np.random.poisson(3, 5000)
plt.hist(poisson_sample)
plt.show()


def poisson_QQ(size):
    poisson_sample = np.random.poisson(3, size)
    sm.qqplot(poisson_sample, line = '45')
    statistic, p_value = stats.shapiro(poisson_sample)
    plt.title(f'n: {size}, p-value: {p_value}')
    plt.show()

poisson_QQ(6000)
poisson_QQ(7000)
poisson_QQ(8000)


