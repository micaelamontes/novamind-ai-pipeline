# NovaMind AI-Powered Marketing Pipeline
_An automated system that generates, distributes, and analyzes marketing content using AI._

**Built by:** Micaela Montes
**Language:** Python  
**Status:** Prototype  
**Purpose:** Demonstrate an AI-driven content engine with automated performance feedback loops.


Overview

Hi there! This project automates the end-to-end marketing content workflow for NovaMind, an early-stage AI startup that helps creative agencies automate their daily workflows.
The system uses AI to generate, distribute, and analyze blog and newsletter content for three personas:

Founders / Decision-Makers – ROI, growth, efficiency

Creative Professionals – inspiration, tools, creativity

Operations Managers – workflows, reliability

It’s a lightweight prototype showing how AI can power a self-improving content engine.


Features

1) AI Content Generation (`ai_content.py`)
- Automatically creates a **400–600 word blog post** and **three persona-specific newsletters**.  
- Each newsletter includes **three variations (A/B/C)** — different tones and phrasing — to simulate real-world copy testing.  
- Variants are stored with each persona under `"revisions"`, enabling experimentation and iterative improvement.  

2) CRM Simulation (`crm.py`)
- Simulates HubSpot-style API calls to “send” newsletters.  
- Randomly selects **A/B/C revisions** to emulate live A/B testing.  
- Logs every send event to `data/mock/hubspot_logs.json` for transparency.  

3) Performance Tracking (`performance.py`)
- Generates random but realistic **open, click, and unsubscribe rates** for each persona.  
- Saves all performance data to `data/metrics/performance_log.csv`.  
- Mimics analytics feedback loops used in real CRM dashboards.  


4) Hands-Free Pipeline (`insights.py`)
- Automatically creates a Markdown report summarizing campaign results:  
  - Top and lowest performing personas  
  - Average engagement rates  
  - Actionable suggestions for the next campaign (“Try numbered subjects,” “Add mini-case visuals,” etc.)  
- Outputs reports in `data/insights/` 

Architecture Overview
src/
 ├── ai_content.py       # Generates blog + multi-revision newsletters (A/B/C)
 ├── crm.py              # Simulates HubSpot CRM operations & logs campaigns
 ├── performance.py      # Simulates engagement metrics & saves CSV logs
 ├── insights.py         # Summarizes results & generates Markdown insights
 ├── run_pipeline.py     # Runs the full automated workflow
 └── __init__.py         # Marks src as a package
data/
 ├── content/            # Generated campaign JSON files
 ├── mock/               # Mock HubSpot log file
 ├── metrics/            # Engagement performance logs (CSV)
 └── insights/           # AI-generated campaign insights (Markdown)
requirements.txt          # Python dependencies
README.md                 # Project documentation


Workflow:

1. Generate content: Blog + newsletter drafts created with persona-specific tone
2. Distribute: Simulated CRM “sends” each newsletter (A/B/C randomized)
3. Track: Randomized engagement metrics logged
4. Analyze: AI-style insights generated with next-step recommendations

After one full run:
- 📝 data/content/cmp_2025-10-20.json – Blog + newsletter dataset
- 💌 data/mock/hubspot_logs.json – “Sent” email logs
- 📊 data/metrics/performance_log.csv – Engagement metrics
- 🧠 data/insights/insights_cmp_2025-10-20.md – AI performance summary



Setup Instructions
1.  Create a virtual environment:
    python3 -m venv .venv
    source .venv/bin/activate
2.  Install dependencies:
    pip install -r requirements.txt
3.  Run the full pipeline:
    python3 -m src.run_pipeline