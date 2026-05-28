# misc-dev-utils
Various utility scripts for development

---

## License

These script are provided as-is. Use at your discretion, feel free to use and modify them for your projects.

---

# Scripts 

---

# Xcode Image Assets Generator

A Python script to generate 1x, 2x, and 3x image assets for Xcode from a single input image. The 3x asset is the same size as the original image, while 1x and 2x are scaled down proportionally.

---

## Requirements

- Python 3.6 or later
- [Pillow](https://python-pillow.org/) library

## Installation

1. **Install Pillow** (if not already installed):
  ```bash
   pip install pillow
  ```
   If you encounter permission issues, use:

## Usage

### Basic Usage

Run the script from the command line, providing the path to your input image:

```bash
python generate_xcode_assets.py input.png
```

This will create a folder named `xcode_assets` in the same directory as your script, containing:

- `image.png` (1x, 1/3 of the original size)
- `image@2x.png` (2x, 2/3 of the original size)
- `image@3x.png` (3x, same as the original size)

### Custom Output Directory

To specify a custom output directory, use the `--output` flag:

```bash
python generate_xcode_assets.py input.png --output my_assets
```

## Example

If your input image is `icon.png` (300x300 pixels), running:

```bash
python generate_xcode_assets.py icon.png
```

Will generate:

- `image.png` (100x100 pixels)
- `image@2x.png` (200x200 pixels)
- `image@3x.png` (300x300 pixels)

## Notes

- The script uses **Lanczos resampling** for high-quality downscaling.
- Supported input formats: PNG, JPEG, and other formats supported by Pillow.
- Output files are always saved as PNG.

## Troubleshooting

### Pillow Not Installed

If you see `ImportError: No module named PIL`, ensure Pillow is installed for the Python version you're using:

```bash
python3 -m pip install pillow
```

### Python Version Issues

If you have multiple Python versions, explicitly use Python 3:

```bash
python3 generate_xcode_assets.py input.png
```

### Permissions

If you encounter permission errors, try installing Pillow locally:

```bash
python3 -m pip install --user pillow
```
