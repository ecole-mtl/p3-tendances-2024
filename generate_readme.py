import os
import re


# RUN IT
# python3 generate_readme.py


# Define the directory containing images and the README file
image_dir = "images"
readme_path = "README.md"

def sanitize_filename(filename):
    """Replace spaces with underscores in filename"""
    return filename.replace(' ', '_')

def rename_files_remove_spaces(directory):
    """Recursively rename files replacing spaces with underscores"""
    renamed_mappings = {}  # Store old->new path mappings
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
                old_path = os.path.join(root, file)
                new_filename = sanitize_filename(file)
                new_path = os.path.join(root, new_filename)
                
                if ' ' in file:
                    try:
                        os.rename(old_path, new_path)
                        relative_old = os.path.relpath(old_path, image_dir)
                        relative_new = os.path.relpath(new_path, image_dir)
                        renamed_mappings[relative_old] = relative_new
                        print(f"Renamed: {relative_old} -> {relative_new}")
                    except OSError as e:
                        print(f"Error renaming {old_path}: {e}")
    
    return renamed_mappings

def get_image_files(directory):
    """Recursively get all image files from directory and its subdirectories"""
    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
                relative_path = os.path.relpath(os.path.join(root, file), image_dir)
                image_files.append(relative_path)
    return sorted(image_files)

# First rename the actual files
renamed_files = rename_files_remove_spaces(image_dir)

# Get all image files recursively
image_files = get_image_files(image_dir)

# Write the README with image tags
with open(readme_path, "w") as readme:
    readme.write("# Réalité future, le contexte\n\n")
    for image in image_files:
        # Use forward slashes for markdown compatibility
        image_path = f"{image_dir}/{image.replace(os.sep, '/')}"
        # Remove any remaining spaces in the path for the markdown
        image_path = image_path.replace(' ', '_')
        readme.write(f"![{image.replace(' ', '_')}]({image_path})\n\n")

print("\nREADME.md has been updated with the new filenames.")