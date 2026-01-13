import os
import sys
from epub_summarizer.core.reader import read_book
from epub_summarizer.services.ai_service import summarize_text
from epub_summarizer.core.converter import text_to_speech

def main():
    """Main function to orchestrate the ebook to audio summary process."""
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_ebook>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Create output directory if it doesn't exist
    output_dir = 'output'
    os.makedirs(output_dir, exist_ok=True)

    book_content = read_book(file_path)
    if book_content:
        summary = summarize_text(book_content)
        if summary:
            # Define output filenames
            base_filename = os.path.splitext(os.path.basename(file_path))[0]
            summary_filepath = os.path.join(output_dir, base_filename + '.txt')
            audio_filepath = os.path.join(output_dir, base_filename + '.mp3')

            # Save the summary text to a file
            try:
                with open(summary_filepath, 'w', encoding='utf-8') as f:
                    f.write(summary)
                print(f"Summary text saved to {summary_filepath}")
            except IOError as e:
                print(f"Error saving summary text file: {e}")
                sys.exit(1)

            # Convert summary to speech
            text_to_speech(summary, audio_filepath)
            print(f"Audio summary saved to {audio_filepath}")

if __name__ == "__main__":
    main()
