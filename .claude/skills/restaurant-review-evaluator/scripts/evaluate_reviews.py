import csv
import sys
from pathlib import Path


REQUIRED_COLUMNS = {"true_label", "predicted_label"}
VALID_LABELS = {"positive", "negative"}


def normalize_label(label):
    if label is None:
        return ""
    return str(label).strip().lower()


def safe_divide(a, b):
    return a / b if b != 0 else 0


def evaluate_reviews(csv_path):
    path = Path(csv_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {csv_path}")

    rows = []
    with path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("The CSV file is empty or has no header row.")

        missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames)
        if missing_columns:
            raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

        for row in reader:
            true_label = normalize_label(row.get("true_label"))
            predicted_label = normalize_label(row.get("predicted_label"))

            if true_label in VALID_LABELS and predicted_label in VALID_LABELS:
                row["true_label"] = true_label
                row["predicted_label"] = predicted_label
                rows.append(row)

    total_valid = len(rows)

    if total_valid == 0:
        raise ValueError("No valid rows found. Labels must be positive or negative.")

    correct = sum(1 for row in rows if row["true_label"] == row["predicted_label"])

    tp = sum(1 for row in rows if row["true_label"] == "negative" and row["predicted_label"] == "negative")
    fp = sum(1 for row in rows if row["true_label"] == "positive" and row["predicted_label"] == "negative")
    fn = sum(1 for row in rows if row["true_label"] == "negative" and row["predicted_label"] == "positive")
    tn = sum(1 for row in rows if row["true_label"] == "positive" and row["predicted_label"] == "positive")

    accuracy = safe_divide(correct, total_valid)
    precision = safe_divide(tp, tp + fp)
    recall = safe_divide(tp, tp + fn)
    f1 = safe_divide(2 * precision * recall, precision + recall)

    mistakes = [
        row for row in rows
        if row["true_label"] != row["predicted_label"]
    ]

    print("# Restaurant Review Evaluation Report")
    print()
    print(f"Total valid reviews: {total_valid}")
    print(f"Correct predictions: {correct}")
    print()
    print("## Metrics")
    print(f"Accuracy: {accuracy:.3f}")
    print(f"Precision: {precision:.3f}")
    print(f"Recall: {recall:.3f}")
    print(f"F1 score: {f1:.3f}")
    print()
    print("## Confusion Summary")
    print(f"True negative reviews correctly predicted as negative: {tp}")
    print(f"Positive reviews incorrectly predicted as negative: {fp}")
    print(f"Negative reviews incorrectly predicted as positive: {fn}")
    print(f"True positive reviews correctly predicted as positive: {tn}")
    print()
    print("## Misclassified Examples")
    if not mistakes:
        print("No misclassified examples found.")
    else:
        for row in mistakes[:10]:
            review_id = row.get("review_id", "N/A")
            platform = row.get("platform", "N/A")
            text = row.get("review_text", "")
            print(f"- Review {review_id} from {platform}")
            print(f"  Text: {text}")
            print(f"  True label: {row['true_label']}")
            print(f"  Predicted label: {row['predicted_label']}")
            print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python evaluate_reviews.py path/to/reviews.csv")
        sys.exit(1)

    evaluate_reviews(sys.argv[1])