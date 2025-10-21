import json
import os
import datetime

# ai_content.py --> Generates AI-powered blog and newsletter content for each persona.
# Part of the NovaMind pipeline for automated marketing content generation.

def generate_content(topic: str, output_dir="data/content"):
    """
    Simulates AI content generation. Takes a topic string and creates:
    - a 500-word blog (fake)
    - 3 short newsletter summaries for different personas with A/B/C revisions
    - Each revision includes a suggestion for improvement
    """

    #Create fake blog text
    blog_body = f"""
    ## {topic}: How AI is Changing the Game

    Artificial Intelligence is transforming how small creative agencies
    operate. By automating repetitive workflows, AI tools save time, reduce
    costs, and boost creativity. NovaMind's automation engine helps teams
    integrate their favorite tools—like Notion, Zapier, and ChatGPT—
    into one seamless platform.

    From client onboarding to project management, automation allows teams
    to focus on strategy and design rather than manual tasks. Over time,
    this shift toward intelligent workflows leads to faster delivery,
    happier clients, and more room for innovation.
    """

    #Create multiple versions (A/B/C) for each persona 
    def generate_variants(base_subject, base_body):
        """Create alternate tones and include suggestions for each revision."""
        return [
            {
                "version": "A",
                "subject": base_subject,
                "body": base_body,
                "suggestion": "Try emphasizing measurable outcomes for this persona."
            },
            {
                "version": "B",
                "subject": base_subject + " – Simplified",
                "body": base_body.replace("automates", "streamlines"),
                "suggestion": "Simplify the headline and focus on ease-of-use benefits."
            },
            {
                "version": "C",
                "subject": "Reimagining Creativity with AI",
                "body": base_body + " NovaMind empowers teams to think bigger.",
                "suggestion": "Make this one more visionary or emotional to appeal to creatives."
            }
        ]

    #Short newsletters for each of the personas
    newsletters = [
        {
            "persona": "Founders",
            "revisions": generate_variants(
                "Boost ROI with AI-powered workflows",
                "Founders love how NovaMind automates routine tasks and integrates seamlessly with tools they already use."
            )
        },
        {
            "persona": "Creative Professionals",
            "revisions": generate_variants(
                "Spark Inspiration with Smart Automation",
                "NovaMind helps creatives focus on ideas, not admin work, freeing up time for bold, original thinking."
            )
        },
        {
            "persona": "Operations Managers",
            "revisions": generate_variants(
                "Seamless Workflows with Reliable AI",
                "Operations teams value NovaMind’s dependable automation that integrates cleanly across systems."
            )
        }
    ]

    #Save output ---
    campaign_id = f"cmp_{datetime.date.today()}"
    output = {
        "campaign_id": campaign_id,
        "topic": topic,
        "blog": {"title": f"{topic} Insights", "body": blog_body.strip()},
        "newsletters": newsletters
    }

    os.makedirs(output_dir, exist_ok=True)
    filepath = f"{output_dir}/{campaign_id}.json"

    with open(filepath, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Content generated and saved to {filepath}")
    return output
