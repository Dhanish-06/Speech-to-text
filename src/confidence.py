import re

def estimate_confidence(transcript: str) -> int:
    if not transcript.strip():
        return 0

    text = transcript.lower()

    # Normalize punctuation
    text = re.sub(r"[^\w\s]", "", text)

    filler_phrases = [
        "um",
        "uh",
        "sooo",
        "hang on",
        "wait i forgot",
        "noise",
        "static"
    ]

    penalty = 0

    for phrase in filler_phrases:
        occurrences = text.count(phrase)
        penalty += occurrences

    # Penalize heavily for hesitation
    confidence = max(40, 100 - penalty * 12)

    return confidence
