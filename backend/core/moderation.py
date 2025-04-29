BAD_WORDS = {"damn", "hell", "stupid", "idiot", "dumb"}

def is_clean(text: str) -> bool:
    text = text.lower()
    return not any(bad_word in text for bad_word in BAD_WORDS)
