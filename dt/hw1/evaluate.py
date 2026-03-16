import pandas as pd
from typing import Tuple, List

def evaluate_predictions(df: pd.DataFrame) -> Tuple[float, dict]:
    correct = (df['label'] == df['deepseek_prediction']).sum()
    total = len(df)
    accuracy = correct / total if total > 0 else 0
    
    label_distribution = df['label'].value_counts().to_dict()
    prediction_distribution = df['deepseek_prediction'].value_counts().to_dict()
    
    print(f"Accuracy: {accuracy:.4f} ({correct}/{total})")
    print(f"\nLabel distribution: {label_distribution}")
    print(f"Prediction distribution: {prediction_distribution}")
    
    return accuracy, {
        'label_distribution': label_distribution,
        'prediction_distribution': prediction_distribution
    }

def identify_errors(df: pd.DataFrame, max_samples: int = 100) -> pd.DataFrame:
    errors = df[df['label'] != df['deepseek_prediction']]
    
    if len(errors) > max_samples:
        errors = errors.sample(n=max_samples, random_state=42)
    
    print(f"\nFound {len(errors)} error samples (max {max_samples})")
    
    return errors

def analyze_error_types(errors: pd.DataFrame) -> dict:
    error_types = {}
    
    for _, row in errors.iterrows():
        error_type = f"{row['label']} -> {row['deepseek_prediction']}"
        error_types[error_type] = error_types.get(error_type, 0) + 1
    
    print("\nError type distribution:")
    for error_type, count in sorted(error_types.items(), key=lambda x: x[1], reverse=True):
        print(f"  {error_type}: {count}")
    
    return error_types

def main():
    df = pd.read_csv('data_with_prediction.csv')
    print(f"Loaded {len(df)} samples with predictions")
    
    accuracy, distributions = evaluate_predictions(df)
    
    errors = identify_errors(df, max_samples=100)
    
    error_types = analyze_error_types(errors)
    
    errors.to_csv('error_samples.csv', index=False)
    print("\nSaved error samples to error_samples.csv")

if __name__ == "__main__":
    main()
