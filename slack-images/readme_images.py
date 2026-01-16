import os

# --- CONFIGURATION ---
IMAGE_SUBFOLDER = 'files'  # The name of your subfolder
README_FILE = 'README.md'  # README in the root
# ---------------------

IMG_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')


def generate_github_readme():
    # Path to look for files
    target_path = os.path.join(os.getcwd(), IMAGE_SUBFOLDER)

    if not os.path.exists(target_path):
        print(f"Error: Subfolder '{IMAGE_SUBFOLDER}' not found.")
        return

    # Get sorted list of images
    files = [f for f in os.listdir(
        target_path) if f.lower().endswith(IMG_EXTENSIONS)]
    files.sort()

    with open(README_FILE, 'w', encoding='utf-8') as md:
        md.write(f"# Image Gallery\n\n")
        md.write(f"Total images: {len(files)}\n\n")

        md.write("| File Name | Preview |\n")
        md.write("| :--- | :--- |\n")

        for filename in files:
            # We prepend the /files/ path to the URL
            # Note: For GitHub relative paths, 'files/filename' is usually safer
            # than '/files/filename' (which looks at the repo root).
            img_url = f"{IMAGE_SUBFOLDER}/{filename}"

            # Format: | filename | ![alt](url) |
            md.write(f"| `{filename}` | ![{filename}]({img_url}) |\n")

    print(
        f"[*] Success! {README_FILE} created. Linked {len(files)} images via /{IMAGE_SUBFOLDER}/")


if __name__ == "__main__":
    generate_github_readme()
