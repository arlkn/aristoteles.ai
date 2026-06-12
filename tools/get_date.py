from langchain_core.tools import tool
import datetime

@tool
def get_current_date() -> str:
    """Returns the current date and time in a human-readable format."""
    now = datetime.datetime.now()
    return f"Şu anki tarih ve saat: {now.strftime('%Y-%m-%d %H:%M:%S')}"
