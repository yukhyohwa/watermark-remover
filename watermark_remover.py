import cv2
import numpy as np
import os
import argparse
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class WatermarkProcessor:
    """
    A professional utility for processing and analyzing blind digital watermarks
    in both frequency (FFT) and spatial domains.
    """
    def __init__(self, input_path: str):
        self.input_path = input_path
        self.img = self._load_image(input_path)

    @staticmethod
    def _load_image(path: str) -> np.ndarray:
        """Safely loads images supporting Unicode/Chinese paths."""
        if not os.path.exists(path):
            raise FileNotFoundError(f"Input file not found: {path}")
        
        img_data = np.fromfile(path, dtype=np.uint8)
        img = cv2.imdecode(img_data, cv2.IMREAD_COLOR)
        
        if img is None:
            raise ValueError(f"Failed to decode image data from: {path}")
        
        return img

    @staticmethod
    def _save_image(img_data: np.ndarray, output_path: str, quality: int = 85) -> None:
        """Safely saves images supporting Unicode/Chinese paths."""
        # Force JPEG extension for compression heuristics
        if not output_path.lower().endswith(('.jpg', '.jpeg')):
            output_path = os.path.splitext(output_path)[0] + '.jpg'

        is_success, im_buf_arr = cv2.imencode('.jpg', img_data, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
        
        if is_success:
            im_buf_arr.tofile(output_path)
            logging.info(f"Image successfully saved to: {output_path}")
        else:
            logging.error(f"Failed to save image to: {output_path}")

    def remove_watermark(self, output_path: str, blur_radius: int = 3, resize_factor: float = 0.99, jpeg_quality: int = 85) -> None:
        """
        Removes blind watermarks using a pipeline of Gaussian blur, micro-resampling,
        and lossy JPEG compression to destroy high-frequency/spatial embedded signals.
        """
        logging.info("Initializing watermark removal pipeline...")
        original_h, original_w = self.img.shape[:2]

        # 1. Filter High Frequency signals via Gaussian Blur
        ksize = blur_radius if blur_radius % 2 != 0 else blur_radius + 1
        processed_img = cv2.GaussianBlur(self.img, (ksize, ksize), 0)
        logging.info(f"Step 1: Applied Gaussian Blur (Kernel: {ksize}x{ksize})")

        # 2. Disrupt grid alignments via Micro-Resampling
        if resize_factor != 1.0:
            new_w, new_h = int(original_w * resize_factor), int(original_h * resize_factor)
            processed_img = cv2.resize(processed_img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
            processed_img = cv2.resize(processed_img, (original_w, original_h), interpolation=cv2.INTER_LINEAR)
            logging.info(f"Step 2: Applied Micro-Resampling (Factor: {resize_factor})")

        # 3. Truncate DCT coefficients via JPEG Compression
        logging.info(f"Step 3: Committing with JPEG Compression (Quality: {jpeg_quality})")
        self._save_image(processed_img, output_path, quality=jpeg_quality)

    def extract_and_visualize(self, output_path: str) -> None:
        """
        Extracts mathematical features to reveal invisible watermarks.
        Outputs a horizontally stacked image:
        [1] Original Grayscale | [2] Frequency Domain (FFT) | [3] Spatial Laplacian
        """
        logging.info("Extracting spatial and frequency domains to reveal watermarks...")
        
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        # 1. Frequency Domain Analysis using FFT
        f = np.fft.fft2(gray)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)
        freq_viz = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        
        # 2. Add cross-hairs for FFT visual guidance
        h, w = freq_viz.shape
        cv2.line(freq_viz, (w//2, 0), (w//2, h), (100,), 1, cv2.LINE_AA)
        cv2.line(freq_viz, (0, h//2), (w, h//2), (100,), 1, cv2.LINE_AA)
        
        # 3. Spatial Domain Analysis using Laplacian Edge Enhancement
        # This helps visualize subtle LSB (Least Significant Bit) or direct spatial overlays
        laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=3)
        lap_viz = cv2.normalize(np.abs(laplacian), None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        lap_viz = cv2.equalizeHist(lap_viz) # Enhance contrast to make faint spatial noises pop

        # Combine visualizations
        combined = np.hstack((gray, freq_viz, lap_viz))
        
        # Save output map
        self._save_image(combined, output_path, quality=95)
        logging.info("Visualization analysis completed successfully.")


def main():
    parser = argparse.ArgumentParser(
        description="Blind Watermark Analysis and Removal Tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-i", "--input", required=True, help="Path to input image")
    parser.add_argument("-o", "--output", required=True, help="Path to save processed image")
    parser.add_argument("--mode", choices=['remove', 'extract'], default='remove', 
                        help="'remove' to destroy watermark, 'extract' to visualize it")
    
    # Removal Specific Args
    removal_group = parser.add_argument_group('Removal Options')
    removal_group.add_argument("-b", "--blur", type=int, default=3, help="Gaussian blur radius (odd number)")
    removal_group.add_argument("-q", "--quality", type=int, default=85, help="JPEG compression quality (1-100)")
    removal_group.add_argument("-r", "--resize", type=float, default=0.99, help="Micro-resampling factor")

    args = parser.parse_args()

    try:
        processor = WatermarkProcessor(args.input)
        
        if args.mode == 'remove':
            processor.remove_watermark(
                output_path=args.output,
                blur_radius=args.blur,
                resize_factor=args.resize,
                jpeg_quality=args.quality
            )
        elif args.mode == 'extract':
            processor.extract_and_visualize(output_path=args.output)
            
    except Exception as e:
        logging.error(f"Process failed: {e}")


if __name__ == "__main__":
    main()
