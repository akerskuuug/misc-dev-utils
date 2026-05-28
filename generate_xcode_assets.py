from PIL import Image
import os
import argparse

def generate_xcode_assets(input_path, output_dir="xcode_assets"):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the input image
    with Image.open(input_path) as img:
        original_width, original_height = img.size

        # 3x is the same as the original
        img_3x = img.copy()
        img_3x.save(os.path.join(output_dir, "image@3x.png"))

        # 2x is 2/3 of the original size
        new_width_2x = int(original_width * 2 / 3)
        new_height_2x = int(original_height * 2 / 3)
        img_2x = img.resize((new_width_2x, new_height_2x), Image.LANCZOS)
        img_2x.save(os.path.join(output_dir, "image@2x.png"))

        # 1x is 1/3 of the original size
        new_width_1x = int(original_width / 3)
        new_height_1x = int(original_height / 3)
        img_1x = img.resize((new_width_1x, new_height_1x), Image.LANCZOS)
        img_1x.save(os.path.join(output_dir, "image.png"))

    print("Assets generated in '{}':".format(output_dir))
    print("- image.png (1x, {}x{})".format(new_width_1x, new_height_1x))
    print("- image@2x.png (2x, {}x{})".format(new_width_2x, new_height_2x))
    print("- image@3x.png (3x, {}x{})".format(original_width, original_height))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Xcode image assets (1x, 2x, 3x) from an input image.")
    parser.add_argument("input", help="Path to the input image file")
    parser.add_argument("--output", help="Output directory (default: xcode_assets)", default="xcode_assets")
    args = parser.parse_args()

    generate_xcode_assets(args.input, args.output)