import os

def create_folder_structure(project_name):
    # Create root directory if it doesn't exist
    if not os.path.exists(project_name):
        os.mkdir(project_name)
        print(f"Created project directory: {project_name}")

    # Define subdirectories
    subdirectories = {
        "data": ["images", "trained_models"],
        "notebooks": [],
        "src": ["preprocessing", "ocr", "sentiment_analysis"],
        "util": []
    }

    # Create subdirectories
    for parent_dir, child_dirs in subdirectories.items():
        parent_path = os.path.join(project_name, parent_dir)
        if not os.path.exists(parent_path):
            os.mkdir(parent_path)
            print(f"Created directory: {parent_path}")

        # Create child directories
        for child_dir in child_dirs:
            child_path = os.path.join(parent_path, child_dir)
            if not os.path.exists(child_path):
                os.mkdir(child_path)
                print(f"Created directory: {child_path}")

    # Create main.py file
    main_file_path = os.path.join(project_name, "main.py")
    if not os.path.exists(main_file_path):
        with open(main_file_path, "w") as main_file:
            main_file.write("# Main script to run the entire pipeline (image processing, OCR, sentiment analysis)")
        print(f"Created main.py: {main_file_path}")

if __name__ == "__main__":
    project_name = "IT-Sentiment"
    create_folder_structure(project_name)