import os
import sys
import concurrent.futures
import logging
from utility.logger_util import LoggerUtil
from ocr_utils import TesseractOCR, TextRecognizer
from utility.utils import get_image_paths

# Initialize logger
logger = LoggerUtil()
logger.init_logger("text_recognizer.log", log_level=logging.INFO)

def recognize_text(image_path, ocr_obj):
    """Recognizes text in the given image and returns the result."""
    try:
        logger.log_info(f"Recognizing text in the image: {image_path}")
        result = ocr_obj.extract_text(image_path)
        logger.log_info(f"Text extraction completed for image: {image_path}")
        return result
    except Exception as e:
        logger.log_error(f"Error processing image {image_path}: {e}")
        return []

if __name__ == "__main__":
    # Check if folder path is provided as command-line argument
    if len(sys.argv) != 2:
        logger.log_error("Usage: python script.py <folder_path>")
        sys.exit(1)
    
    # Get folder path from command-line argument
    folder_path = sys.argv[1]
    
    # Check if folder exists
    if not os.path.isdir(folder_path):
        logger.log_error("Error: Invalid folder path.")
        sys.exit(1)
    
    # Initialize TextRecognizer object
    text_recognizer = TextRecognizer(languages=['en'])
    t_ocr = TesseractOCR()
    
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Process images in parallel using ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_image_path = {executor.submit(recognize_text, image_path,text_recognizer): image_path 
                                for image_path in get_image_paths(folder_path)}
        for future in concurrent.futures.as_completed(future_to_image_path):
            image_path = future_to_image_path[future]
            try:
                result = future.result()
                # Concatenate recognized text into a single string
                text = ' '.join(result)
                # Print recognized text for the image
                print("Extracted text ------------------------------------------------")
                print(f"Image: {image_path}, Text: {text}")
                print("Extracted text ------------------------------------------------")
            except Exception as e:
                logger.log_error(f"Error processing image {image_path}: {e}")