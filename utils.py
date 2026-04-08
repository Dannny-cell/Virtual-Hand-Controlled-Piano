def format_notes(notes):
    return " ".join(sorted(note.upper() for note in notes)) if notes else ""
