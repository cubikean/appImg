# README

## Image Compressor

This Python script provides a simple GUI application for compressing images in bulk. It supports converting images to different formats (JPG, WEBP, PNG) and allows users to customize compression options.

### Usage

1. **Select Image Folder**: Click the "Folder To Convert" button to choose the folder containing the images you want to compress.

2. **Select Destination Folder**: Click the "Destination Folder" button to choose the folder where the compressed images will be saved.

3. **Choose Output Format(s)**: Select the desired output format(s) by checking the corresponding checkboxes (JPG, WEBP, PNG).

4. **Set Compression Options**: Adjust the compression options by specifying the compression ratio and quality percentage.

5. **Click "Create The Survey"**: Press the "Create The Survey" button to initiate the image compression process.

### Requirements

- Python 3.x
- tkinter library

### How to Run

1. Clone the repository:

    ```bash
    git clone https://github.com/cubikean/appImg.git
    cd appImg
    ```

2. Run the script:

    ```bash
    python appImg.py
    ```

### Dependencies

This script depends on the `compress_image_v2` module, which includes functions for collecting and compressing images. Ensure that the `compress_image_v2` module is available in the same directory as the script.

### Example

```python
# Example usage
from compress_image_v2 import collect_img, compress_img

# Define image folder, result folder, and compression options
img_folder = "/path/to/input/images"
result_folder = "/path/to/output/images"
jpg = True
webp = False
png = True
ratio = 0.9
quality = 75

# Collect and compress images
compress_img(images=collect_img(img_folder), destination=result_folder, new_size_ratio=ratio, quality=quality, to_jpg=jpg, to_webp=webp, to_png=png)
