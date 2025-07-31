def is_exit_command(text):
    keywords = ["exit", "quit", "bye", "end", "stop"]
    return any(kw in text.lower() for kw in keywords)
