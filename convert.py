import os
from PIL import Image

# Specify the folder containing your images
folder_path = 'python-statistika/hypotezy/assets/statistika-1-assets'

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if file is a WebP image
    if filename.lower().endswith('.png'):
        file_path = os.path.join(folder_path, filename)
        # Open the image using Pillow
        with Image.open(file_path) as img:
            # Prepare a new filename with .png extension
            base_name = os.path.splitext(filename)[0]
            new_filename = base_name + '.png'
            new_filepath = os.path.join(folder_path, new_filename)
            # Save the image in PNG format
            img.save(new_filepath, 'PNG')
            print(f"Converted {filename} to {new_filename}")
