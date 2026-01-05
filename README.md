# Epub Audio Summarizer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![AI](https://img.shields.io/badge/AI-Gemini-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**Epub Audio Summarizer** is a Python tool designed to convert EPUB books into concise audio summaries. It leverages the **Google Gemini API** for intelligent summarization and **gTTS (Google Text-to-Speech)** to generate audio files, making it easier to consume book content on the go.

## Features / 功能

1.  **Smart EPUB Parsing**: Extracts textual content effectively from EPUB files.
2.  **AI Summarization**: Uses **Google Gemini** (`gemini-flash` model) to generate high-quality summaries.
3.  **Audio Generation**: Converts the text summary into an audio file (`.mp3`).
    *   *Default Language*: Chinese (Traditional/Taiwan) - `zh-tw`.
4.  **Dual Output**: Saves both the text summary (`.txt`) and audio (`.mp3`) for offline access.

## Requirements / 依赖

*   Python 3.x
*   Google Gemini API Key
*   `gTTS` (Google Text-to-Speech)
*   `ebooklib`
*   `beautifulsoup4`

## Installation / 安装

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

## Usage / 使用方法

Run the script by providing the path to your EPUB file:

```bash
python main.py "path/to/your/book.epub"
```

### Output
The script generates results in the `output/` directory:
*   `[book_name].txt`: The text summary.
*   `[book_name].mp3`: The audio summary.

## Project Structure / 项目结构

```text
epub-audio-summarizer/
├── main.py             # Entry point / 主程序
├── book_reader.py      # EPUB content extraction
├── summarizer.py       # AI processing using Gemini API
├── audio_converter.py  # Audio generation (gTTS)
├── .env.example        # Environment variable template
├── requirements.txt    # Project dependencies
└── README.md
```

## License

[MIT](LICENSE)
