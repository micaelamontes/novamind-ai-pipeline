import json, random, datetime
from pathlib import Path
import pandas as pd


# performance.py --> Simulates newsletter performance metrics (open, click, unsubscribe rates).
# Logs and summarizes simulated engagement data for the NovaMind content pipeline.

# Path to save performance logs
PERF_PATH = Path("data/metrics/performance_log.csv")
PERF_PATH.parent.mkdir(parents=True, exist_ok=True)

def simulate_performance(content_bundle: dict):
    """
    Simulate email performance metrics (open rate, click rate, unsubscribe).
    Each persona gets random but reasonable engagement rates.
    """

    results = []
    for nl in content_bundle["newsletters"]:
        persona = nl["persona"]

        #generate random engagement data
        open_rate = round(random.uniform(0.35, 0.65), 2)
        click_rate = round(open_rate * random.uniform(0.2, 0.5), 2)
        unsubscribe_rate = round(random.uniform(0.005, 0.02), 3)

        results.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "campaign_id": content_bundle["campaign_id"],
            "persona": persona,
            "open_rate": open_rate,
            "click_rate": click_rate,
            "unsubscribe_rate": unsubscribe_rate
        })

    #Save to CSV
    df = pd.DataFrame(results)
    if PERF_PATH.exists():
        df.to_csv(PERF_PATH, mode="a", header=False, index=False)
    else:
        df.to_csv(PERF_PATH, index=False)

    print(f"Simulated performance data saved to {PERF_PATH}")
    return df


def summarize_performance(df: pd.DataFrame):
    """
    Generate a simple AI-style insight summary.
    """
    best = df.sort_values(by="click_rate", ascending=False).iloc[0]
    worst = df.sort_values(by="click_rate", ascending=True).iloc[0]

    insight = (
        f"Campaign {best['campaign_id']} Summary:\n"
        f"- {best['persona']} audience had the highest click rate ({best['click_rate']*100:.1f}%).\n"
        f"- {worst['persona']} had the lowest click rate ({worst['click_rate']*100:.1f}%).\n"
        f"Suggestion: Next campaign, consider reusing {best['persona']}'s tone or structure to improve engagement."
    )

    print(insight)
    return insight
