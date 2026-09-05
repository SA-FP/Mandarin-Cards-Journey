"""
profilesManda.py
-----------------------------------------
This file handles WHO is using the app.

Three ideas here, all built on st.secrets (the same safe place the Kost app
keeps its password — never written in the code):

1. app_password   -> the front door. Everyone types this first.
2. profiles       -> each learner has their own name and their own password,
                     like picking a user on Netflix or YouTube.
3. dev_password   -> the Dev Console master key, which can open any profile.

IMPORTANT, so nobody is surprised later: the Dev Console can read every
profile's progress. That is what a master key means. If you share this app
with friends, tell them the console exists — a hidden master key is the kind
of thing that breaks trust.
"""

import streamlit as st


def get_profiles():
    """
    Read the list of profiles from Secrets.

    Expected shape in Secrets (TOML):

        [profiles.peter]
        password = "peter123"
        display = "Peter"

        [profiles.mom]
        password = "mom456"
        display = "Mom"

    Returns a dict like {"peter": {"password": "...", "display": "Peter"}}
    """
    raw = st.secrets.get("profiles", {})
    out = {}
    for key in raw:
        entry = raw[key]
        out[key] = {
            "password": str(entry.get("password", "")),
            "display": str(entry.get("display", key.title())),
        }
    return out


def check_app_password(typed):
    """The front door. Returns True if the shared app password is correct."""
    real = st.secrets.get("app_password", "")
    return bool(real) and typed == real


def check_profile_password(profile_key, typed):
    """Returns True if this profile's own password is correct."""
    profiles = get_profiles()
    if profile_key not in profiles:
        return False
    real = profiles[profile_key]["password"]
    return bool(real) and typed == real


def check_dev_password(typed):
    """
    The Dev Console master key.

    Deliberately separate from app_password: knowing the front-door password
    should NOT be enough to read everyone's data.
    """
    real = st.secrets.get("dev_password", "")
    return bool(real) and typed == real


def display_name(profile_key):
    """Friendly name for a profile, falling back to the key itself."""
    profiles = get_profiles()
    if profile_key in profiles:
        return profiles[profile_key]["display"]
    return profile_key


def profile_avatar(profile_key):
    """
    Pick an emoji avatar for a profile, chosen from its name so that the
    same profile always gets the same face (no randomness = no surprises).
    """
    faces = ["🐼", "🐯", "🦊", "🐨", "🐸", "🦉", "🐧", "🐢", "🦄", "🐙"]
    total = sum(ord(c) for c in profile_key)
    return faces[total % len(faces)]
