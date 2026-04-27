---
name: restaurant-review-evaluator
description: Evaluates restaurant review sentiment classification results from a CSV file by computing accuracy, precision, recall, and F1 score, and identifying misclassified examples. Use this when the user asks to evaluate, analyze, or audit classification performance on tabular review data.
---

## When to use this skill

Use this skill when:
- The user provides a CSV file containing restaurant reviews
- The user wants to evaluate sentiment classification performance
- The user asks for metrics such as accuracy, precision, recall, or F1 score
- The user wants to identify classification errors or misclassified examples
- The task involves structured tabular data with true and predicted labels

---

## When NOT to use this skill

Do NOT use this skill when:
- The user asks to generate or predict sentiment labels from scratch
- The user wants a full restaurant review analysis system
- The user asks for business decisions such as compensation or strategy
- There is no structured CSV input with labels
- The task is purely descriptive or does not require computation

---

## Expected inputs

The input should be a CSV file with at least the following columns:

- review_text: the content of the review
- true_label: the ground truth sentiment label
- predicted_label: the model’s predicted sentiment label

Optional columns may include:
- review_id
- platform
- rating
- confidence

---

## Step-by-step instructions

1. Validate that the input is a CSV file
2. Check that required columns exist: true_label and predicted_label
3. Load the CSV using the Python script
4. Clean the data:
   - Remove rows with missing labels
   - Normalize label formats (e.g., Positive → positive)
5. Compute evaluation metrics:
   - accuracy
   - precision
   - recall
   - F1 score
6. Identify misclassified examples
7. Return a structured evaluation report
8. Provide a short explanation of the results

---

## Expected output format

The output should include:

- total number of reviews
- number of valid rows used
- accuracy
- precision
- recall
- F1 score
- confusion summary (optional)
- a few misclassified examples
- a short natural language summary of performance

---

## Limitations and checks

- This skill does not determine whether labels are correct; it only compares them
- It assumes the input CSV is reasonably clean and structured
- It may not handle complex sentiment cases such as sarcasm or mixed sentiment perfectly
- It should not be used to make automated business decisions
- It depends on the correctness of provided labels

---

## Role of the script

The Python script is required to:
- parse and validate the CSV file
- perform deterministic metric calculations
- ensure consistent and accurate results

This cannot be reliably done with natural language alone.