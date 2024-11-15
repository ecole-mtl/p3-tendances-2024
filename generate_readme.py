import os

# Define the directory containing images and the README file
image_dir = "images"  # Change to your images folder
readme_path = "README.md"

# Get a list of image file names in the image directory
image_files = [f for f in os.listdir(image_dir) if f.endswith((".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf"))]

# Write the README with image tags
with open(readme_path, "w") as readme:
    readme.write("# Réalité future, le contexte\n\n")
    for image in image_files:
        image_path = f"{image_dir}/{image}"
        readme.write(f"![{image}]({image_path})\n\n")
