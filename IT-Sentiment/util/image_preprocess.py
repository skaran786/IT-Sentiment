import argparse
import cv2
from pathlib import Path
from logger_util import LoggerUtil

class ImagePreprocessor:
    def __init__(self, target_size=(256, 256), log_file="preprocessing.log"):
        self.target_size = target_size
        self.logger = LoggerUtil(log_file)

    def preprocess_image(self, image_path, output_dir):
        """Preprocess an image"""
        try:
            # Read the image
            image = cv2.imread(str(image_path))

            # Resize the image
            resized_image = cv2.resize(image, self.target_size, interpolation=cv2.INTER_LINEAR)

            # Save the preprocessed image
            output_path = output_dir / image_path.name
            cv2.imwrite(str(output_path), resized_image)
            self.logger.log_info(f"Preprocessed image saved at: {output_path}")

        except Exception as e:
            self.logger.log_error(f"Error preprocessing image {image_path}: {str(e)}")