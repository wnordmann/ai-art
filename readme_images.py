import os

# --- CONFIGURATION ---
# Folder containing your images
IMAGE_DIR = './review_graphs' 
# The name of the markdown file to create
README_FILE = os.path.join(IMAGE_DIR, 'README.md')
# ---------------------

# Supported image extensions
IMG_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')

def generate_gallery():
    if not os.path.exists(IMAGE_DIR):
        print(f"Error: Folder '{IMAGE_DIR}' not found.")
        return

    # Get sorted list of images
    files = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(IMG_EXTENSIONS)]
    files.sort()

    with open(README_FILE, 'w', encoding='utf-8') as md:
        md.write(f"# Image Gallery: {os.path.basename(IMAGE_DIR)}\n\n")
        md.write(f"Total images found: {len(files)}\n\n")
        
        # Create a table for a neat grid layout (3 columns)
        md.write("| Image Name | Preview |\n")
        md.write("| :--- | :--- |\n")
        
        for filename in files:
            # GitHub renders images using standard Markdown syntax
            # We use the filename as the Alt-text
            img_line = f"| `{filename}` | ![{filename}]({filename}) |\n"
            md.write(img_line)

    print(f"[*] Success! {README_FILE} created with {len(files)} images.")

if __name__ == "__main__":
    generate_gallery()