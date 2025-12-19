# Epub2AudioSummary

A Python script to convert EPUB books into concise audio summaries using the Google Gemini API and gTTS (Google Text-to-Speech).

## Features

- Reads text content from EPUB files.
- Uses the Gemini API (`gemini-flash-latest`) to generate a summary of the book.
- Converts the generated summary into a Chinese (zh-tw) audio file (`.mp3`).
- Saves both the text summary (`.txt`) and the audio file (`.mp3`) into an `output` directory.

## Requirements

- Python 3.x
- A Google Gemini API Key

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yukhyohwa/Epub2AudioSummary.git
    cd Epub2AudioSummary
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your environment variables:**
    Create a file named `.env` in the root of the project and add your Gemini API key. You can also rename the provided `.env.example` file to `.env` and fill in your key.
    ```env
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

## Usage

Run the script from your terminal by providing the path to your EPUB file:

```bash
python main.py "path/to/your/book.epub"
```

## Output

The script will generate two files in the `output/` directory:
- `[book_name].txt`: The text summary.
- `[book_name].mp3`: The audio version of the summary.
