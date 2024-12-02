
# Bayes classifier

## Overview
This project implements a **Naive Bayes classifier** to categorize books into six predefined categories based on their title and description. The categories are:

1. کلیات اسلام (General Islamic Studies)
2. مدیریت و کسب و کار (Management and Business)
3. داستان کودک و نوجوانان (Children and Adolescent Stories)
4. رمان (Novels)
5. داستان کوتاه (Short Stories)
6. جامعه‌شناسی (Sociology)

The project is written in Python and leverages text preprocessing and machine learning concepts, including the Hazm library for Persian language processing.

---

## Files and Structure
### Data Files:
- **`books_train.csv`**: Contains the training dataset with titles, descriptions, and categories of books.
- **`books_test.csv`**: Contains the test dataset used to evaluate the classifier.

### Scripts:
1. **`CA0_1.py`**: 
   - Uses dictionaries (`dict_cat_1`, ..., `dict_cat_6`) to implement the bag-of-words model for each category.
   - Calculates probabilities for classification using a log-based Naive Bayes formula.
   - Prints the accuracy of the model on the test set.

2. **`CA0_2.py`**:
   - Utilizes lists (`list_cat_1`, ..., `list_cat_6`) to store words for each category.
   - Implements the same logic as `CA0_1.py` but focuses on list-based operations.
   - Provides an alternative implementation with potential accuracy and efficiency differences.

### Documentation:
- **`EPS_CA0_F23_V1.pdf`**: The problem statement, theory, and instructions for the project. It explains the use of Bayes' theorem, preprocessing steps, and evaluation methods.
- **`گزارش پروژه صفر امار و احتمال.pdf`**: Project report detailing preprocessing methods, challenges, results, and alternative implementations.

---

## Methodology
1. **Text Preprocessing**:
   - Normalizing text (removing unnecessary spaces and normalizing characters).
   - Removing punctuation.
   - Tokenizing text into words.
   - Lemmatizing words (reducing them to their root form).
   - Removing stop words (non-informative words such as prepositions).

2. **Bag-of-Words (BoW) Model**:
   - Extracts word counts for each category.
   - Represents text data as vectors based on word frequency.

3. **Naive Bayes Classifier**:
   - Applies Bayes' theorem to calculate the likelihood of each category for a given book.
   - Utilizes additive smoothing to handle unseen words in the test dataset.
   - Uses log probabilities to prevent underflow in calculations.

4. **Evaluation**:
   - Compares predicted categories against the actual labels in `books_test.csv`.
   - Calculates and outputs accuracy.

---

## Usage
### Requirements
- Python 3.x
- Required Libraries: `pandas`, `numpy`, `hazm`, `math`

### How to Run
1. Install dependencies:
   ```bash
   pip install pandas numpy hazm
   ```
2. Place the `books_train.csv` and `books_test.csv` files in the same directory as the script.
3. Run one of the scripts:
   ```bash
   python CA0_1.py
   ```
   or
   ```bash
   python CA0_2.py
   ```

### Output
The scripts print the accuracy of the classifier on the test dataset.

---

## Results
- Accuracy of the first implementation (`CA0_1.py`): **76%**
- Accuracy of the second implementation (`CA0_2.py`): **82%**

**Trade-offs**:
- The dictionary-based implementation (`CA0_1.py`) is faster but less accurate.
- The list-based implementation (`CA0_2.py`) offers higher accuracy at the cost of increased runtime.

---

## Future Improvements
1. **Feature Engineering**:
   - Use advanced preprocessing techniques like stemming.
   - Explore bigrams or trigrams for better context understanding.

2. **Optimization**:
   - Enhance runtime efficiency of the list-based implementation.
   - Experiment with other smoothing techniques.

3. **Evaluation**:
   - Use additional metrics like precision, recall, and F1-score for a more detailed evaluation.

---

For further details, refer to the project documentation in the PDF files provided.
