"""
cloud_storeManda.py
-----------------------------------------
Saves each learner's progress to GitHub, exactly like the Kost app does.

The difference here: instead of one blob of data, everything is stored
per profile:

    {
      "profiles": {
        "peter": {"known": ["\u4e00", "\u4e8c"], "seen": 40, "correct": 31, "wrong": 9},
        "mom":   {"known": [],                   "seen": 0,  "correct": 0,  "wrong": 0}
      }
    }

"known" is the list of characters that learner has marked as learned.

New concept compared with the Kost app: read_only_data(). The Dev Console
uses it to look at a profile WITHOUT loading it as the current user, so
browsing someone's progress can never accidentally overwrite it.
"""

import base64
import json
import requests
import streamlit as st


def _headers():
    token = st.secrets["github_token"]
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
    }


def _api_url():
    repo = st.secrets["github_repo"]           # example: "SA-FP/mandarin-cards"
    path = st.secrets.get("data_file_path", "mandarin_data.json")
    return f"https://api.github.com/repos/{repo}/contents/{path}"


def default_data():
    """The starting shape of the database: no profiles have studied anything yet."""
    return {"profiles": {}}


def blank_profile():
    """
    The starting progress for one learner.

    "known"    -> characters they have marked as learned
    "chapters" -> results of the end-of-chapter tests, keyed by chapter number
                  as a STRING (JSON has no integer keys), e.g.
                  {"1": {"best": 90, "attempts": 2, "passed": True}}
    """
    return {"known": [], "seen": 0, "correct": 0, "wrong": 0, "chapters": {}}


def load_data():
    """Fetch the whole database from GitHub (all profiles)."""
    resp = requests.get(_api_url(), headers=_headers(), timeout=15)

    if resp.status_code == 200:
        content = resp.json()
        decoded = base64.b64decode(content["content"]).decode("utf-8")
        return json.loads(decoded)

    if resp.status_code == 404:
        # No file exists yet -> create an empty one
        data = default_data()
        save_data(data)
        return data

    raise RuntimeError(f"Failed to fetch data from GitHub ({resp.status_code}): {resp.text}")


def save_data(data):
    """Save the whole database back to GitHub (creates 1 new commit)."""
    get_resp = requests.get(_api_url(), headers=_headers(), timeout=15)
    sha = get_resp.json()["sha"] if get_resp.status_code == 200 else None

    content_str = json.dumps(data, indent=2, ensure_ascii=False)
    encoded = base64.b64encode(content_str.encode("utf-8")).decode("utf-8")

    payload = {"message": "Update Mandarin progress", "content": encoded}
    if sha:
        payload["sha"] = sha

    put_resp = requests.put(_api_url(), headers=_headers(), json=payload, timeout=15)
    if put_resp.status_code not in (200, 201):
        raise RuntimeError(f"Failed to save data to GitHub ({put_resp.status_code}): {put_resp.text}")


def get_profile(data, profile_key):
    """Get one learner's progress, creating a blank one if they are new."""
    if "profiles" not in data:
        data["profiles"] = {}
    if profile_key not in data["profiles"]:
        data["profiles"][profile_key] = blank_profile()
    return data["profiles"][profile_key]
