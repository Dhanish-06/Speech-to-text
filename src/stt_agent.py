import os
from utils import get_client

def transcribe_audio(audio_path: str) -> str:
    client = get_client()

    with open(audio_path, "rb") as audio:
        response = client.audio.transcriptions.create(
            file=audio,
            model=os.getenv("AZURE_OPENAI_TRANSCRIBE_DEPLOYMENT")
        )

    return response.text
