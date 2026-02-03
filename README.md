# Epub Audio Summarizer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![AI](https://img.shields.io/badge/AI-Gemini-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**Epub Audio Summarizer** is a Python tool designed to convert EPUB books into concise audio summaries. It leverages the **Google Gemini API** for intelligent summarization and **gTTS (Google Text-to-Speech)** to generate audio files, making it easier to consume book content on the go.

## Features

1.  **Smart EPUB Parsing**: Extracts textual content effectively from EPUB files.
2.  **AI Summarization**: Uses **Google Gemini** (`gemini-flash` model) to generate high-quality summaries.
3.  **Audio Generation**: Converts the text summary into an audio file (`.mp3`).
    *   *Default Language*: Chinese (Traditional/Taiwan) - `zh-tw`.
4.  **Dual Output**: Saves both the text summary (`.txt`) and audio (`.mp3`) for offline access.

## Requirements

*   Python 3.x
*   Google Gemini API Key
*   `gTTS` (Google Text-to-Speech)
*   `ebooklib`
*   `beautifulsoup4`

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yukhyohwa/epub-audio-summarizer.git
    cd epub-audio-summarizer
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuration**:
    Create a `.env` file in the root directory and add your API key:
    ```ini
    GEMINI_API_KEY=your_api_key_here
    ```

## Usage

Run the script by providing the path to your EPUB file:

```bash
python src/main.py "data/books/your_book.epub"
```

### Output
The script generates results in the `output/` directory:
*   `[book_name].txt`: The text summary.
*   `[book_name].mp3`: The audio summary.

## Project Structure

```text
epub-audio-summarizer/
├── data/                  # Storage for input files
│   └── books/             # EPUB books to process
├── src/                   # Source code
│   ├── main.py            # Entry point
│   └── epub_summarizer/   # Core Package
│       ├── core/          # Parsing and logic
│       │   ├── reader.py     # EPUB extraction
│       │   └── converter.py  # Audio generation
│       ├── services/      # AI services
│       │   └── ai_service.py # Gemini API processing
│       └── config.py      # Configuration and Constants
├── output/                # Generated summaries and audio
├── .env                   # API keys (Local)
├── .env.example
├── requirements.txt
└── README.md
```

## License

[MIT](LICENSE)
