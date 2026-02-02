from dotenv import load_dotenv
load_dotenv()

import os
from validator import validate_audio
from stt_agent import transcribe_audio
from confidence import estimate_confidence


# Resolve absolute path safely
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO_DIR = os.path.join(BASE_DIR, "audio_samples")


def list_audio_files():
    if not os.path.exists(AUDIO_DIR):
        raise FileNotFoundError(f"Audio directory not found: {AUDIO_DIR}")

    return [
        f for f in os.listdir(AUDIO_DIR)
        if f.lower().endswith(".wav")
    ]


def main():
    print("Resolved AUDIO_DIR:", AUDIO_DIR)

    files = list_audio_files()
    if not files:
        print("No audio files found.")
        return

    print("\nAvailable audio files:\n")
    for idx, file in enumerate(files, start=1):
        print(f"{idx}. {file}")

    try:
        choice = int(input("\nSelect file number to transcribe: "))
        selected_file = files[choice - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    audio_path = os.path.join(AUDIO_DIR, selected_file)

    validate_audio(audio_path)

    print("\n--- TRANSCRIBING ---")
    transcript = transcribe_audio(audio_path)
    print(transcript)

    print("\n--- CONFIDENCE ---")
    confidence = estimate_confidence(transcript)
    print(f"Confidence Score: {confidence}%")

    if confidence < 70:
        print("⚠️ Low confidence — audio may be unclear.")


if __name__ == "__main__":
    main()
