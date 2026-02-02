def validate_audio(file_path: str):
    if not file_path.lower().endswith(".wav"):
        raise ValueError("Only .wav files are supported")

    return True
