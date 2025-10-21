import json, glob
from src.ai_content import generate_content
from src.crm import send_newsletters
from src.performance import simulate_performance, summarize_performance

# run_pipeline.py --> Main orchestrator that runs the full AI marketing pipeline end-to-end.
# Generates content, sends newsletters (mocked), simulates performance, and saves insights.


def run_full_pipeline(topic: str):
    """
    Full end-to-end automation:
    1. Generate AI blog + newsletters
    2. Send (simulated) via CRM
    3. Log & summarize performance
    """

    print("Starting AI-powered content pipeline...\n")

    #Step 1: Generate content
    content = generate_content(topic)
    print("\n Content generation complete.")

    #Step 2: Send newsletters via simulated CRM 
    send_newsletters(content)
    print("\n  CRM distribution complete.")

    #Step 3: Simulate & summarize performance 
    df = simulate_performance(content)
    summarize_performance(df)

    print("\n Pipeline finished successfully!\n")

if __name__ == "__main__":
    #Example topic
    run_full_pipeline("AI in Creative Automation")
