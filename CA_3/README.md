# Statistical Analysis and Probabilistic Modeling with Python

## Overview

This repository contains three Python programs along with a dataset (`FIFA2020.csv`) and a pretrained autoencoder model (`mnist_AE.h5`). The project is structured around key statistical and probabilistic concepts:

1. **Mean Squared Error (MSE) and Autoencoders**
2. **Regression and Least Squares**
3. **Central Limit Theorem and Sampling**

## Directory Structure

```
EPS_CA3/
├── 1.py                # Autoencoder MSE and distribution analysis
├── 2.py                # Regression and outlier effects
├── 3.py                # Central Limit Theorem and sampling distribution
├── FIFA2020.csv        # FIFA player stats dataset
├── mnist_AE.h5         # Pretrained autoencoder model
└── EPS_CA#3.pdf        # Project description and requirements
```

## 1. Autoencoder & MSE (File: `1.py`)

- Loads the MNIST dataset and a pretrained autoencoder from `mnist_AE.h5`
- Reconstructs test images and calculates the MSE for all 10,000 examples
- Visualizes sample reconstructions
- Performs statistical analysis:
  - MSE histogram
  - Kolmogorov-Smirnov test to assess if the MSE values are normally distributed

## 2. Regression and Outlier Analysis (File: `2.py`)

- Manually implements least squares linear regression on datasets with:
  - Outliers
  - High leverage points
  - Both
- Calculates R² for each scenario
- Plots regression lines alongside original and modified data
- Explores how outliers and leverage points distort the regression line

## 3. Central Limit Theorem & Sampling (File: `3.py`)

- Loads and cleans the `FIFA2020.csv` dataset
  - Handles missing values in `pace` and `dribbling` columns
- Generates boxplots and statistical summaries for the `age` column
- Draws samples of sizes 100, 500, and 2000 from the `weight` column
  - Computes mean, variance, standard deviation
  - Plots Q-Q plots for normality comparison
  - Runs Shapiro-Wilk test to assess normality
- Simulates Poisson distributions and compares them with normal distributions using Q-Q plots and p-values