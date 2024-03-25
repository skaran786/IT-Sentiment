import argparse
from pathlib import Path
from image_preprocess_util import ImagePreprocessor

def main():
    parser = argparse.ArgumentParser(description="Image preprocessing script")
    parser.add_argument("input_dir", type=Path, help="Input directory containing images")
    parser.add_argument("output_dir", type=Path, help="Output directory for preprocessed images")
    parser.add_argument("--target_size", type=int, nargs=2, default=(256, 256),
                        help="Target size for resizing (width height)")
    args = parser.parse_args()

    # Initialize ImagePreprocessor
    preprocessor = ImagePreprocessor(target_size=tuple(args.target_size))

    # Process each image in the input directory
    for image_path in args.input_dir.glob("*"):
        if image_path.is_file():
            preprocessor.preprocess_image(image_path, args.output_dir)

if __name__ == "__main__":
    main()
