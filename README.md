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


## What the script does

The Python script:
- loads and validates the CSV file
- checks required columns
- cleans and normalizes labels
- computes evaluation metrics (accuracy, precision, recall, F1)
- identifies misclassified reviews
- outputs a structured evaluation report

This ensures accurate and consistent results that cannot be achieved through natural language alone.

---

## What worked well

- The skill was correctly discovered and activated by the agent
- The Python script handled the deterministic computation reliably
- The integration between the skill and the agent was smooth
- The output was clear, structured, and useful for analysis

---

## What limitations remain

- The skill assumes the input CSV is correctly formatted
- It only supports binary sentiment (positive / negative)
- It does not handle complex sentiment cases such as sarcasm
- It should not be used for making business decisions (e.g., refunds or penalties)

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