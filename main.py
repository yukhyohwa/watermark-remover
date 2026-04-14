import argparse
import logging
import sys
from core.processor import WatermarkProcessor

# Configure global logging formatting
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler(sys.stdout)]
)

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
    removal_group = parser.add_argument_group('Removal Options (Only applies if mode="remove")')
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
