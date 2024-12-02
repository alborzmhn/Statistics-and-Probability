import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as ss
import numpy as np
df = pd.read_csv(r"C:\Users\Mahmodiyan-PC\Desktop\amar ehtemal\CA_2\Tarbiat.csv")
metro = list(df.loc[:, "metro"])
brt = list(df.loc[:, "BRT"])
#plt.hist(metro)
#plt.hist(brt)

lambda_metro = sum(metro) / len(metro)
lambda_brt = sum(brt) / len(brt)

poisson_metro = ss.poisson.pmf(list(range(0, 25)), lambda_metro)

#plt.plot(poisson_metro)
#plt.hist(metro, density = True)

lambda_Z = lambda_metro + lambda_brt
poisson_Z = ss.poisson.pmf(list(range(0, 25)), lambda_Z)
#plt.plot(poisson_z)
#plt.hist(metro + brt, density = True)

W_binomial = ss.binom.pmf(list(range(0, 25)), 8, lambda_metro / lambda_Z)
#plt.plot(w_binomial)

sum_metro_brt  = np.array(metro) + np.array(brt)

index = []
for i in range(len(sum_metro_brt)):
    if sum_metro_brt[i] == 8: index.append(i)

metro_in = []
for i in range(len(metro)):
    if i in index: metro_in.append(metro[i])

plt.hist(metro_in, density=True)
plt.plot(W_binomial)
plt.show()