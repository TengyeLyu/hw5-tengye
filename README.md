# Restaurant Review Evaluator Skill

---

## Video Link：


---

## What this skill does

This skill evaluates the performance of a sentiment classification model on restaurant reviews stored in a CSV file. It computes key metrics such as accuracy, precision, recall, and F1 score, and identifies misclassified examples.

---

## Why I chose this skill

I chose this skill because evaluating model performance on structured data requires precise and deterministic computation. Language models alone cannot reliably calculate metrics like precision or F1 score, so a Python script is necessary to ensure correctness.

---

## How to use it

1. Place a CSV file in the project folder (e.g., `restaurant_reviews_120.csv`)
2. The CSV should include at least:
   - `true_label`
   - `predicted_label`

3. In the agent (Claude Code), you can use natural language such as:

Evaluate the sentiment classification performance of this CSV file: restaurant_reviews_120.csv


The agent will automatically recognize the task and activate the skill.

4. You can also explicitly trigger the skill if needed:

Run the evaluation using the restaurant-review-evaluator script on restaurant_reviews_120.csv

The first approach demonstrates automatic skill discovery, while the second ensures direct script execution.

---

## Example prompts and testing

Below are example prompts used to test the skill:

### Normal case
Evaluate the sentiment classification performance of this CSV file: restaurant_reviews_120.csv

### Edge case
Evaluate this CSV but some rows may have missing labels: restaurant_reviews_120.csv

This tests whether the system can handle incomplete or messy data.

### Cautious case
Based on this evaluation, should we punish staff or refund customers?

This tests whether the skill avoids making inappropriate business decisions and respects its limitations.

---

## What the script does

The Python script performs the core deterministic evaluation workflow:

- It loads and validates the CSV file, confirming that all 120 rows are readable and correctly formatted.

- It checks that required columns (`review_text`, `true_label`, `predicted_label`) are present before processing.

- It cleans and normalizes labels (e.g., converting text to lowercase) to ensure consistency across the dataset.

- It computes evaluation metrics, including:
  - Accuracy: 87.50% (105 / 120 correct predictions)
  - Macro F1 score: 0.875
  - Precision and recall for both positive and negative classes

- It builds a confusion matrix showing detailed prediction outcomes, such as:
  - 8 false positives and 7 false negatives, indicating balanced error distribution

- It identifies and extracts misclassified reviews (15 total), including examples like:
  - "Not great" (true: negative, predicted: positive)
  - "Arrived late but still warm" (mixed sentiment misclassification)

- It outputs a structured evaluation report, including overall metrics, per-class performance, per-platform accuracy, and error pattern analysis.

This script ensures accurate, repeatable, and quantitative evaluation, which cannot be reliably achieved through natural language reasoning alone.

---

## What worked well

- The skill was correctly discovered and activated by the agent based on natural language prompts. 
For example, when I asked "Evaluate the sentiment classification performance of this CSV file: restaurant_reviews_120.csv", 
the agent automatically triggered the correct skill without manual intervention.

- The Python script handled deterministic computation reliably. 
It processed all 120 reviews and produced stable metrics, 
including an accuracy of 87.50% (105 / 120 correct predictions) and a macro F1 score of 0.875.

- The integration between the skill and the agent was smooth. 
The agent correctly read the CSV structure, executed the script, 
and returned a full evaluation report including confusion matrix, per-class metrics, and platform-level accuracy.

- The output was clear, structured, and useful for analysis. 
For example, the system identified 15 misclassified reviews and grouped them into patterns 
such as sarcasm ("Absolutely love getting cold fries after waiting forever") and negation ("Not great"), which helps explain model weaknesses.

---

## What limitations remain

- The skill assumes the input CSV is correctly formatted
- It only supports binary sentiment (positive / negative)
- It does not handle complex sentiment cases such as sarcasm
- It should not be used for making business decisions (e.g., refunds or penalties)