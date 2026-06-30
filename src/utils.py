import datetime

def log_message(message: str):
    """Simple logger with timestamp."""
    print(f"[{datetime.datetime.now()}] {message}")
