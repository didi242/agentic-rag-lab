from langchain.tools import tool
from data.person_db import PERSON_PROFILE_DB, PERSON_EVENTS_DB


@tool
def get_person(person: str) -> dict:
    """Returns full structured person data including profile and events."""

    profile = PERSON_PROFILE_DB.get(person.lower())
    events = PERSON_EVENTS_DB.get(person.lower(), [])

    if not profile:
        return {
            "person": person,
            "error": "unknown",
            "profile": None,
            "events": []
        }

    return {
        "person": person,
        "profile": profile,
        "events": events
    }