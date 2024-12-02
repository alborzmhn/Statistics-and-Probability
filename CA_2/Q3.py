import random
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as pld

digits_data = pd.read_csv(r"C:\Users\Mahmodiyan-PC\Desktop\amar ehtemal\CA_2\digits.csv")

label_201 = digits_data.loc[200]
digits_data = digits_data.drop(200)
label_202 = digits_data.loc[201]
digits_data = digits_data.drop(201)

for row in digits_data:
    for pixel in row:
        if pixel < "128":
            pixel = 0
        else :
            pixel = 1

row = digits_data.loc[random.randint(0, len(digits_data) - 1)]
row = np.reshape(row[1:], (28, 28))
pld.imshow(row)
pld.show()