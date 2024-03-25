import logging
from logging.handlers import RotatingFileHandler
import sys
from functools import wraps

class LoggerUtil:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LoggerUtil, cls).__new__(cls)
            cls._instance.logger = None
        return cls._instance

    def init_logger(self, log_file, log_level=logging.INFO, max_size=10*1024*1024, backup_count=5):
        """Initialize logger configuration"""
        if not self.logger:
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(log_level)

            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

            # Log to file
            file_handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

            # Log to console
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def set_log_level(self, log_level):
        """Set logging level dynamically"""
        if self.logger:
            self.logger.setLevel(log_level)

    def set_log_format(self, log_format):
        """Set log format"""
        if self.logger:
            for handler in self.logger.handlers:
                handler.setFormatter(logging.Formatter(log_format))

    def log_info(self, message):
        """Log an info message"""
        if self.logger:
            self.logger.info(message)

    def log_error(self, message):
        """Log an error message"""
        if self.logger:
            self.logger.error(message)

def with_logging(func):
    """Decorator to log function calls"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger = LoggerUtil()
        logger.log_info(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        logger.log_info(f"Function {func.__name__} execution completed")
        return result

    return wrapper

if __name__ == "__main__":
    logger = LoggerUtil()
    logger.init_logger("example.log")
    logger.set_log_level(logging.DEBUG)
    logger.set_log_format('%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    @with_logging
    def example_function():
        print("Example function called")

    example_function()
