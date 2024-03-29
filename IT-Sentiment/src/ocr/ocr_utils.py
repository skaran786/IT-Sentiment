import io
from utility.logger_util import LoggerUtil
import logging
import easyocr
import pytesseract
from PIL import Image

# Initialize logger
logger = LoggerUtil()
logger.init_logger("text_recognizer.log", log_level=logging.INFO)

class TextRecognizer:
    def __init__(self, languages=['en']):
        self.languages = languages
        self.reader = None  # lazy initialization
    
    def _get_reader(self):
        if self.reader is None:
            self.reader = easyocr.Reader(self.languages)
            logger.log_info("Initialized easyocr.Reader")
        return self.reader
    
    def recognize_text(self, image_path):
        """
        Recognizes text in the given image and returns the result.
        
        Args:
        - image_path: Path to the image file.
        
        Returns:
        - A list of tuples, each containing the recognized text and its bounding box coordinates.
        """
        logger.log_info(f"Recognizing text in the image: {image_path}")
        reader = self._get_reader()
        result = reader.readtext(image_path)
        logger.log_info("Text recognition completed")
        return result
    
    def extract_text(self, image_path):
        """
        Extracts and returns the recognized text from the given image.
        
        Args:
        - image_path: Path to the image file.
        
        Returns:
        - A list of recognized text strings.
        """
        logger.log_info(f"Extracting text from the image: {image_path}")
        result = self.recognize_text(image_path)
        text_list = [text_info[1] for text_info in result]
        logger.log_info("Text extraction completed")
        return text_list
    
    def get_text_with_coordinates(self, image_path):
        """
        Returns the recognized text along with its bounding box coordinates from the given image.
        
        Args:
        - image_path: Path to the image file.
        
        Returns:
        - A list of tuples, each containing the recognized text, its bounding box coordinates, and confidence score.
        """
        logger.log_info(f"Getting text with coordinates from the image: {image_path}")
        result = self.recognize_text(image_path)
        logger.log_info("Text with coordinates retrieval completed")
        return result

# Example usage:
if __name__ == "__main__":
    # Example image path
    image_path = 'example_image.jpg'
    
    # Initialize TextRecognizer object
    text_recognizer = TextRecognizer(languages=['en'])
    
    # Recognize text
    text_and_coords = text_recognizer.get_text_with_coordinates(image_path)
    
    # Print recognized text and its bounding box coordinates
    for text, bbox, _ in text_and_coords:
        print(f"Text: {text}, Bounding Box: {bbox}")

class TesseractOCR:
    def __init__(self, tesseract_cmd=None):
        """
        Initialize Tesseract OCR.

        Args:
            tesseract_cmd (str): Path to the Tesseract executable. If None, pytesseract will use the system default.
        """
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def extract_text(self, image_path):
        """
        Extract text from an image.

        Args:
            image_path (str): Path to the image file.

        Returns:
            str: Extracted text.
        """
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text

    def extract_text_from_bytes(self, image_bytes):
        """
        Extract text from an image represented as bytes.

        Args:
            image_bytes (bytes): Image data in bytes format.

        Returns:
            str: Extracted text.
        """
        image = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(image)
        return text