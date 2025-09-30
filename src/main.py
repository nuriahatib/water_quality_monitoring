from load_data import load_csv
from clean_data import clean_sensor_data
from evaluate import WaterQualityEvaluator
import pandas as pd

def main():
    # 1. Load data
    df = load_csv("data/sensor_data.csv")

    if df.empty:
        print("No data to process.")
        return

    # 2. Clean data
    df = clean_sensor_data(df)

    # 3. Evaluate
    evaluator = WaterQualityEvaluator()

    results = []
    for _, row in df.iterrows():
        safe, reason = evaluator.is_safe(row)
        status = "Safe" if safe else f"Unsafe ({reason})"
        print(f"{row['sensor_id']} at {row['timestamp']}: {status}")

        # Collect results for optional saving
        results.append({
            "sensor_id": row["sensor_id"],
            "timestamp": row["timestamp"],
            "pH": row["pH"],
            "turbidity": row["turbidity"],
            "status": "Safe" if safe else "Unsafe",
            "reason": reason
        })

    # 4. (Optional) Save to CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv("data/results.csv", index=False)
    print("\nResults saved to data/results.csv")

if __name__ == "__main__":
    main()
