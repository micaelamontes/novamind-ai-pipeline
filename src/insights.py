import pandas as pd
from pathlib import Path
from datetime import datetime

# insights.py — Generates Markdown performance insights and recommendations.
# Uses simulated data to suggest next steps for content optimization.


INSIGHTS_DIR = Path("data/insights")
INSIGHTS_DIR.mkdir(parents=True, exist_ok=True)

def generate_insights(df: pd.DataFrame, campaign_id: str) -> Path:
    """
    Takes a DataFrame with columns:
      persona, version, open_rate, click_rate, unsubscribe_rate, suggestion (optional)
    Writes a short Markdown report and returns its file path.
    """

    #Keep only relevant columns if they exist
    cols = [col for col in ["persona", "version", "open_rate", "click_rate", "unsubscribe_rate", "suggestion"] if col in df.columns]
    df = df[cols].copy()

    #Calculate key stats
    best = df.sort_values("click_rate", ascending=False).iloc[0]
    worst = df.sort_values("click_rate", ascending=True).iloc[0]
    avg_click = df["click_rate"].mean()

    #AI-powered content improvement suggestions
    tests = [
        f"Reuse tone/structure from **{best.persona} (Version {getattr(best, 'version', 'A')})** in weaker segments.",
        "Try a numbered subject line (e.g., '3 ways…') and keep it under 45 characters.",
        "Add one visual mini-case (before→after) near the top CTA.",
        "Test a verb-first CTA: 'Get', 'Try', 'See'."
    ]

    #Generate Markdown
    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    md = [
        f"# Campaign {campaign_id} – Performance Insights",
        f"*Generated: {ts}*",
        "",
        "## Highlights",
        f"- **Top click rate:** {best.persona} (Version {getattr(best, 'version', 'A')}) – {best.click_rate*100:.1f}%",
        f"- **Lowest click rate:** {worst.persona} (Version {getattr(worst, 'version', 'A')}) – {worst.click_rate*100:.1f}%",
        f"- **Average click rate (all):** {avg_click*100:.1f}%",
        "",
        "## Recommendations (next tests)",
        *[f"- {t}" for t in tests],
        "",
        "## Persona Metrics",
        "| Persona | Version | Open Rate | Click Rate | Unsub Rate | Suggestion |",
        "|---|:---:|---:|---:|---:|:---|",
    ]

    #Add each row of metrics
    for _, r in df.iterrows():
        suggestion = getattr(r, "suggestion", "")
        version = getattr(r, "version", "A")
        md.append(
            f"| {r.persona} | {version} | {r.open_rate*100:.1f}% | {r.click_rate*100:.1f}% | {r.unsubscribe_rate*100:.2f}% | {suggestion} |"
        )

    #Save file
    out_path = INSIGHTS_DIR / f"insights_{campaign_id}.md"
    out_path.write_text("\n".join(md), encoding="utf-8")
    print(f"🧠 Insights saved to {out_path}")
    return out_path


if __name__ == "__main__":
    import json, glob
    from src.performance import simulate_performance

    #Load latest campaign content
    fp = sorted(glob.glob("data/content/*.json"))[-1]
    cb = json.load(open(fp))
    df = simulate_performance(cb)
    generate_insights(df, cb["campaign_id"])