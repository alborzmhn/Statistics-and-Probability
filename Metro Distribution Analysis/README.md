# BRT and Metro Distribution Analysis

## Overview
This project aims to analyze the distribution of the number of BRT (Bus Rapid Transit) and Metro passes at the Tabriz-Madras station during specific time intervals. The dataset, `csv.tarbiat`, contains the number of passes for both BRT and Metro in various time intervals. The goal is to explore the data using statistical methods like plotting histograms, identifying distributions, fitting distributions, and performing Bayesian inference.

---

## Tasks and Methodology

### 1. **Histogram Plotting**
   - **Objective**: Draw histograms for both metro and BRT pass counts.
   - **Method**: 
     - Use `matplotlib` to create histograms for each dataset.
     - Visualize the frequency distribution of the passes.

### 2. **Identifying the Distribution of Variables**
   - **Objective**: Determine the distribution of the two variables: X (metro passes) and Y (BRT passes).
   - **Method**: 
     - Based on the histograms and the nature of the data, identify the distribution (e.g., Poisson, Normal) and calculate their parameters.
     - Use statistical methods and visualizations to hypothesize the underlying distributions.

### 3. **Discrete Distribution Plot**
   - **Objective**: Plot the histogram density for the metro pass count.
   - **Method**: 
     - Use `matplotlib` to plot the histogram density for the 'metro' column in the dataset.

### 4. **Fit Distribution to Data**
   - **Objective**: Fit a theoretical distribution to the data using Scipy and verify the model.
   - **Method**: 
     - Using `scipy.stats`, fit the identified distribution (from Task 2) to the data.
     - Plot the fitted distribution on top of the histogram to validate the model.

### 5. **Summing Distributions (X + Y = Z)**
   - **Objective**: Define a new random variable \( Z = X + Y \) and analyze its distribution.
   - **Method**: 
     - Calculate the distribution parameters for \( Z \).
     - Plot the distribution of \( Z \) and compare it with the sum of metro and BRT passes.

### 6. **Wald Distribution**
   - **Objective**: Define a new variable \( W = X + Y | X(P) \sim W \) and calculate its distribution.
   - **Method**: 
     - Derive the theoretical distribution of \( W \) using appropriate formulas and calculate its parameters.

### 7. **Plotting the Wald Distribution**
   - **Objective**: Plot the probability mass function for the Wald distribution.
   - **Method**: 
     - Use `scipy.stats` to plot the PMF of the derived Wald distribution with the parameters.

### 8. **Conditional Distribution**
   - **Objective**: Visualize the conditional distribution of metro passes, given the total count of metro and BRT passes.
   - **Method**: 
     - Add the conditional distribution of metro passes to the graph and analyze the results.

---

## Dataset
The dataset, `csv.tarbiat`, contains two columns:
- **Metro**: The number of metro passes recorded at various time intervals.
- **BRT**: The number of BRT (bus rapid transit) passes recorded at the same intervals.

Each row in the dataset represents the pass counts at a specific time interval.

---

## Libraries Used
- **Matplotlib**: For plotting histograms and visualizations.
- **SciPy**: For statistical analysis, including distribution fitting and plotting.
- **NumPy**: For numerical calculations, especially for generating random samples and performing statistical operations.
- **SymPy**: For symbolic mathematics and solving equations (especially in Task 6 and Task 7).

---

## Code Explanation

### Task 1 (`Q1.py`) - **Histogram Plotting**
```python
# The code generates a histogram to visualize the distribution of passes for both Metro and BRT.
import numpy as np
import matplotlib.pyplot as plt

# Function to generate samples from a binomial distribution
def sampleBin(m, n, probability):
    matrix = random.choice([0, 1], p = [1 - probability, probability], size = (m, n))
    return np.sum(matrix, axis=1)

# Generate and plot histograms for metro and BRT data
# The histogram is used to understand the frequency distribution of the data
