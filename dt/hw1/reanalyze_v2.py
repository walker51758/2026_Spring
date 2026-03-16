import pandas as pd
from sentiment_analysis import predict_sentiment_batch
from evaluate import evaluate_predictions
import json

OPTIMIZED_PROMPT_V2 = """Analyze the sentiment of the following financial news text. Classify it as POSITIVE, NEUTRAL, or NEGATIVE.

Important guidelines:
1. Factual financial statements with NO subjective words = NEUTRAL (e.g., "Revenue was $500M", "Operating margin was 10%")
2. Statements about business EXPANSION, growth, improvement = POSITIVE
3. Statements about LOSSES, declines, problems = NEGATIVE
4. Compare losses: REDUCED loss = POSITIVE (e.g., "loss of $0.4M compared to $1.9M" = POSITIVE)
5. High margins/synergies in business context = POSITIVE
6. Board decisions (dividends, profit distribution) without evaluation = NEUTRAL

Text: {text}

Respond with only one word: positive, neutral, or negative."""

def reanalyze_with_optimized_prompt_v2() -> dict:
    df = pd.read_csv('llm_data.csv')
    print(f"Loaded {len(df)} samples")
    
    print(f"\nUsing optimized prompt v2")
    
    df_optimized = predict_sentiment_batch(df, prompt=OPTIMIZED_PROMPT_V2)
    
    df_optimized.to_csv('data_with_optimized_prediction_v2.csv', index=False)
    print(f"\nSaved optimized predictions to data_with_optimized_prediction_v2.csv")
    
    accuracy, distributions = evaluate_predictions(df_optimized)
    
    df_original = pd.read_csv('data_with_prediction.csv')
    original_accuracy, _ = evaluate_predictions(df_original)
    
    results = {
        'original_accuracy': original_accuracy,
        'optimized_accuracy': accuracy,
        'improvement': accuracy - original_accuracy,
        'original_distribution': distributions['label_distribution'],
        'optimized_distribution': df_optimized['deepseek_prediction'].value_counts().to_dict()
    }
    
    with open('comparison_results_v2.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print("\n=== Comparison Results ===")
    print(f"Original accuracy: {original_accuracy:.4f}")
    print(f"Optimized accuracy: {accuracy:.4f}")
    print(f"Improvement: {results['improvement']:.4f} ({results['improvement']*100:.2f}%)")
    
    return results

def main():
    results = reanalyze_with_optimized_prompt_v2()

if __name__ == "__main__":
    main()
