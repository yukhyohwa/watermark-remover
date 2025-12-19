from gtts import gTTS

def text_to_speech(text, output_filename):
    """Converts the given text to speech and saves it to a file."""
    try:
        tts = gTTS(text=text, lang='zh-tw')
        tts.save(output_filename)
    except ImportError:
        print("Please install gTTS: pip install gTTS")
    except Exception as e:
        print(f"An error occurred during text-to-speech conversion: {e}")
