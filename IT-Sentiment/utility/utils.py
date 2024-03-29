import os

def get_image_paths(folder_path):
    """Generator function to yield image paths from the specified folder."""
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Filter image files
            yield os.path.join(folder_path, filename)