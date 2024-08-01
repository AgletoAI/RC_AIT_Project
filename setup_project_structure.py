import os

def create_directory_structure(base_path):
    # Define the directory structure
    structure = {
        "data": ["raw", "processed", "external"],
        "notebooks": ["exploration", "development"],
        "src": ["data", "models", "utils"],
        "models": [],
        "reports": ["figures"],
        "tests": [],
    }

    # Create the base project directory
    os.makedirs(base_path, exist_ok=True)

    # Create the subdirectories
    for key, subdirs in structure.items():
        # Create the main directory
        main_dir = os.path.join(base_path, key)
        os.makedirs(main_dir, exist_ok=True)

        # Create any subdirectories
        for subdir in subdirs:
            os.makedirs(os.path.join(main_dir, subdir), exist_ok=True)

    # Create additional files like README.md and .gitignore
    with open(os.path.join(base_path, "README.md"), "w") as f:
        f.write("# Project Title\n\n")
        f.write("## Project Description\n")
        f.write("Describe your project here.\n")

    with open(os.path.join(base_path, ".gitignore"), "w") as f:
        f.write("# Ignore data files\n")
        f.write("/data/raw/\n")
        f.write("/data/processed/\n")
        f.write("/models/\n")
        f.write("/__pycache__/\n")
        f.write("/*.ipynb_checkpoints\n\n")
        f.write("# Ignore virtual environments\n")
        f.write(".venv/\n")
        f.write("env/\n")

    print(f"Project structure created at: {base_path}")

if __name__ == "__main__":
    base_path = os.path.join("C:\\HarryAITime", "ProjectTemplate")
    create_directory_structure(base_path)
