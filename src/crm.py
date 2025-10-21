# crm.py —-> Simulates HubSpot CRM operations (contact upsert, email send, and campaign logging).
# Mock CRM integration used for testing and content distribution in the NovaMind pipeline.

import json, datetime
import random
from pathlib import Path
MODE = "mock"
LOG_PATH = Path("data/mock/hubspot_logs.jsonl")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)


def _log_api_call(operation: str, payload: dict):
    """Append one JSON line that looks like a HubSpot API request."""
    entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "mode": MODE,
        "operation": operation,
        "payload": payload,
    }
    with LOG_PATH.open("a") as f:
        f.write(json.dumps(entry) + "\n")


def _log_api_call(operation: str, payload: dict):
    """Append one JSON line that looks like a HubSpot API request."""
    entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "mode": MODE,
        "operation": operation,
        "payload": payload,
    }
    with LOG_PATH.open("a") as f:
        f.write(json.dumps(entry) + "\n")

def upsert_contact(contact: dict):
    """Pretend to create/update a contact in HubSpot."""
    #HubSpot properties:
    payload = {
        "properties": {
            "email": contact.get("email", ""),
            "firstname": contact.get("first_name", ""),
            "lastname": contact.get("last_name", ""),
            "jobtitle": contact.get("job_title", ""),
            "company": contact.get("company", ""),
            "persona": contact.get("persona", ""),
        }
    }
    _log_api_call("contacts.create_or_update", payload)
    #Return a fake id like HubSpot 
    return {"id": f"hs_contact_{abs(hash(payload['properties']['email'])) % 10_000}"}

def ensure_persona_list(persona: str):
    """Pretend to ensure a static list exists for a persona segment."""
    payload = {"name": f"List - {persona}", "persona": persona}
    _log_api_call("lists.ensure", payload)
    return {"listId": f"list_{persona.lower().replace(' ', '_')}"}

def create_email(subject: str, html: str, name: str):
    """Pretend to create a marketing email draft."""
    payload = {"emailName": name, "subject": subject, "html": html}
    _log_api_call("emails.create", payload)
    return {"emailId": f"hs_email_{abs(hash(subject+name)) % 10_000}"}

def send_email(email_id: str, list_id: str):
    """Pretend to send an email to a list/segment."""
    payload = {"emailId": email_id, "contactListId": list_id}
    _log_api_call("emails.send", payload)
    return {"sendId": f"send_{email_id}_{list_id}"}

def send_newsletters(content_bundle: dict):
    """
    High-level helper:
    - ensures a list for each persona
    - creates an email per persona
    - 'sends' it to that list
    """
    for nl in content_bundle["newsletters"]:
        persona = nl["persona"]
        list_info = ensure_persona_list(persona)
        #Handle multiple revisions (A/B/C) 
        # Handle multiple revisions (A/B/C) safely with random selection
        revisions = nl.get("revisions", [])
        if revisions:
            chosen_rev = random.choice(revisions)  # randomly pick A, B, or C
            subject = chosen_rev.get("subject", f"Update for {persona}")
            body = chosen_rev.get("body", "")
            chosen_label = chosen_rev.get("version", "?")
        else:
            subject = nl.get("subject", f"Update for {persona}")
            body = nl.get("body", "")
            chosen_label = "default"

        email = create_email(
            subject=subject,
            html=body,
            name=f"{content_bundle['campaign_id']}-{persona}-v{chosen_label}"
        )
    print(f"📧 Sent version {chosen_label} to {persona}")

    send_email(email["emailId"], list_info["listId"])
        
    print(f"Simulated CRM: logged to {LOG_PATH}")

