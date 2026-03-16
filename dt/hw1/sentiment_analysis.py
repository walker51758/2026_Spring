import pandas as pd
import requests
import json
import time
from typing import List

DEEPSEEK_API_KEY = "sk-17f892b39933471ea545fc7b3bfdb07a"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

def call_deepseek_api(text: str, prompt: str = None) -> str:
    if prompt is None:
        prompt = "Please analyze the sentiment of the following news text. Respond with only one word: 'positive', 'negative', or 'neutral'.\n\nText: {text}"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a sentiment analysis expert. Classify news texts as 'positive', 'negative', or 'neutral'."},
            {"role": "user", "content": prompt.format(text=text)}
        ],
        "temperature": 0.1,
        "max_tokens": 10
    }
    
    try:
        response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        
        prediction = result["choices"][0]["message"]["content"].strip().lower()
        
        if "positive" in prediction:
            return "positive"
        elif "negative" in prediction:
            return "negative"
        elif "neutral" in prediction:
            return "neutral"
        else:
            return "unknown"
    
    except Exception as e:
        print(f"Error calling DeepSeek API: {e}")
        return "error"

def predict_sentiment_batch(df: pd.DataFrame, prompt: str = None, batch_size: int = 10) -> pd.DataFrame:
    predictions = []
    
    for idx, row in df.iterrows():
        print(f"Processing {idx + 1}/{len(df)}")
        prediction = call_deepseek_api(row['text'], prompt)
        predictions.append(prediction)
        
        if (idx + 1) % batch_size == 0:
            time.sleep(1)
    
    df['deepseek_prediction'] = predictions
    return df

def main():
    df = pd.read_csv('llm_data.csv')
    print(f"Loaded {len(df)} samples")
    
    df_with_prediction = predict_sentiment_batch(df)
    
    df_with_prediction.to_csv('data_with_prediction.csv', index=False)
    print(f"Saved predictions to data_with_prediction.csv")
    
    print("\nPrediction distribution:")
    print(df_with_prediction['deepseek_prediction'].value_counts())

if __name__ == "__main__":
    main()
