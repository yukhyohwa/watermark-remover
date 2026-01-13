from gtts import gTTS
from .. import config

def text_to_speech(text, output_filename):
    """Converts the given text to speech and saves it to a file."""
    try:
        tts = gTTS(text=text, lang=config.DEFAULT_LANGUAGE)
        tts.save(output_filename)
    except Exception as e:
        print(f"An error occurred during text-to-speech conversion: {e}")
