
# Distribution Analyzer

## Overview
This project explores probability distributions, including Binomial, Poisson, and Normal distributions, through Python-based simulations and calculations. It leverages mathematical theories and programming to illustrate key statistical concepts.

The project contains four main exercises:

1. **Binomial Distribution Sampling**: Relationship between Bernoulli and Binomial distributions.
2. **Poisson and Normal Approximations**: Approximation of Binomial distribution under specific conditions.
3. **Normal Distribution Analysis**: Statistical questions based on a Normal distribution.
4. **Further Poisson and Normal Approximations**: Extending approximations with a larger dataset.

---

## Files and Structure
### Scripts:
1. **`Q1.py`**: 
   - Simulates samples from a Binomial distribution.
   - Visualizes theoretical and empirical mean and variance for varying success probabilities.

2. **`Q2.py`**:
   - Simulates and plots a Binomial distribution with Poisson and Normal approximations.
   - Compares the three distributions.

3. **`Q3.py`**:
   - Solves statistical questions based on a Normal distribution, including percentiles and probabilities.

4. **`Q4.py`**:
   - Extends `Q2.py` to larger datasets for Poisson and Normal approximations of Binomial distributions.

### Documentation:
- **`CA#1.pdf`**: Detailed instructions and problem descriptions for each exercise.
- **`گزارش کار.pdf`**: A report summarizing the implementation and results.

---

## Methodology
1. **Binomial Distribution Analysis**:
   - Generates samples using `numpy.random.choice` instead of nested loops for efficiency.
   - Computes theoretical and empirical mean and variance.

2. **Poisson and Normal Approximations**:
   - Approximates a Binomial distribution as Poisson when \( p \) is small and \( n \) is large.
   - Approximates a Binomial distribution as Normal when \( np \) and \( n(1-p) \) are sufficiently large.

3. **Normal Distribution Questions**:
   - Uses cumulative distribution functions (CDFs) to find probabilities and percentiles.
   - Calculates interquartile ranges and probability ranges.

4. **Visualization**:
   - Plots all results for comparison using `matplotlib`.

---

## Usage
### Requirements
- Python 3.x
- Required Libraries: `numpy`, `scipy`, `matplotlib`

### How to Run
1. Install dependencies:
   ```bash
   pip install numpy scipy matplotlib
   ```
2. Run each script independently:
   ```bash
   python Q1.py
   python Q2.py
   python Q3.py
   python Q4.py
   ```

### Output
- Each script generates visual plots and outputs numerical results to the console.

---

## Results
### Highlights:
1. **Empirical vs. Theoretical Analysis**:
   - Empirical mean and variance align with theoretical predictions for large sample sizes.

2. **Approximations**:
   - Poisson approximation performs well for small \( p \), large \( n \).
   - Normal approximation aligns closely for sufficiently large \( np \) and \( n(1-p) \).

3. **Statistical Insights**:
   - Confidence intervals, percentiles, and probabilities provide practical applications of the Normal distribution.

---

## Future Improvements
1. **Interactive Visualizations**:
   - Integrate interactive tools like `Plotly` for better data exploration.

2. **Parameter Optimization**:
   - Automate the identification of optimal conditions for approximations.

3. **Performance**:
   - Optimize large dataset processing to handle real-world scale data efficiently.
