from setuptools import setup, find_packages

setup(
    name='IT-Sentiment',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # List your dependencies here
        'easyocr',
        'pytesseract',
        'Pillow'
    ],
)
