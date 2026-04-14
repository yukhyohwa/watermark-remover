# Frequency Domain Watermark Analyzer & Remover

An open-source desktop utility for detecting, analyzing, and physically eradicating hidden "blind watermarks". It uses a combination of dimensional graphic transformations to destroy digital tracking signals embedded in spatial grids and frequency domains (FFT/DCT).

## Directory Structure

```text
watermark-remover/
├── core/
│   ├── __init__.py
│   └── processor.py      # Core watermark processing logic (WatermarkProcessor)
├── input/                # Recommended folder for input images (ignored by .gitignore)
├── output/               # Recommended folder for output images (ignored by .gitignore)
├── main.py               # CLI entry point
├── requirements.txt
└── README.md
```

## Core Features

* **Extract & Detect (`extract` mode)**: Calculates the Fast Fourier Transform (FFT) spectrum combined with a Laplacian filter in the spatial domain to visualize invisible high-frequency signals or LSB noises.
* **Physical Eradication (`remove` mode)**: Applies **Gaussian frequency truncation** -> **Micro-resampling grid disruption** -> **DCT characteristic formatting** to achieve irreversible, physical-level sanitization against watermarks.

## Requirements

* Python 3.7+
* OpenCV
* NumPy

## Quick Start

```bash
git clone https://github.com/yukhyohwa/watermark-remover.git
cd watermark-remover
pip install -r requirements.txt
```

## Usage

The entry point for the script is `main.py` located in the root directory.

### 1. Scan & Detect Watermarks (`--mode extract`)
When you suspect a screenshot contains a hidden watermark, run the extraction command:
```bash
python main.py --mode extract -i "input/screenshot.png" -o "output/analysis.jpg"
```
*This command outputs a 1:3 comparison image (`analysis.jpg`) containing: Original Grayscale | Frequency Domain FFT Spectrum Heatmap | Spatial Domain Laplacian Sharpening. If unnatural symmetric bright spots appear in the FFT spectrum, it is 100% certain that a frequency-domain watermark exists in the image.*

### 2. Clean & Sanitize (`--mode remove`)
Clean the hidden watermark using default settings (maximizes preservation of original readability):
```bash
python main.py --mode remove -i "input/screenshot.png" -o "output/clean.jpg"
```

**Advanced Cleaning Parameters:**
If you require absolute security and want to bypass highly robust modern watermarks (sacrificing some image quality):
```bash
python main.py --mode remove -i "input/screenshot.png" -o "output/ultra_clean.jpg" -b 5 -q 70 -r 0.98
```

### Full CLI Parameters

* `-i`, `--input`: Path to the input image. (Required)
* `-o`, `--output`: Path to save the processed output image. (Required)
* `--mode`: Execution mode. `remove` (sanitize) or `extract` (detection analysis). Default: `remove`.
* `-b`, `--blur`: [Removal Mode Only] Gaussian blur kernel size. Must be an odd number. Default: `3`.
* `-q`, `--quality`: [Removal Mode Only] Final JPEG lossy compression quality (1-100). Default: `85`.
* `-r`, `--resize`: [Removal Mode Only] Micro-resampling factor to disrupt grid alignments. Default: `0.99`.

## Disclaimer
This project is intended solely for academic research and to enhance developers' understanding of information-hiding technologies. Due to the rapid advancement of modern watermark techniques (e.g., GAN-based hiding), this tool cannot provide absolute anonymity guarantees against judicial-level tracking systems with ultra-high robustness. For top-tier security of sensitive information, physical optical screen recording (taking a photo of the screen) remains the recommended approach.
