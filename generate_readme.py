import os

# Define the directory containing images and the README file
image_dir = "images"  # Change to your images folder
readme_path = "README.md"

def get_image_files(directory):
    """Recursively get all image files from directory and its subdirectories"""
    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
                # Get the relative path from the image_dir
                relative_path = os.path.relpath(os.path.join(root, file), image_dir)
                image_files.append(relative_path)
    return sorted(image_files)  # Sort files for consistent output

# Get all image files recursively
image_files = get_image_files(image_dir)

# Write the README with image tags
with open(readme_path, "w") as readme:
    readme.write("# Réalité future, le contexte\n\n")
    for image in image_files:
        # Use forward slashes for markdown compatibility
        image_path = f"{image_dir}/{image.replace(os.sep, '/')}"
        readme.write(f"![{image}]({image_path})\n\n")