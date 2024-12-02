import scipy.stats as sc
import numpy as np

average = 80
srandard_deviation = 12
normal = sc.norm(average, srandard_deviation * srandard_deviation)

cdf_0 = 0
cdf_grade = cdf_0 + 0.9
question1 = sc.norm.ppf(cdf_grade, average, srandard_deviation)

charak_dovom = sc.norm.ppf(0.75, average, srandard_deviation)
charak_sevom = sc.norm.ppf(0.5, average, srandard_deviation)
question2 = [charak_dovom, charak_sevom]

question3 = normal.cdf(90) - normal.cdf(80)

