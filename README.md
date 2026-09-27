# Image to PDF Converter

A simple Python command-line tool that converts JPG and JPEG images into a PDF file.

## Features

- Convert a single JPG or JPEG image into a PDF.
- Convert multiple JPG/JPEG images from a folder into one PDF.
- Automatically process images in filename order.
- Choose a custom output PDF filename.
- Validate input paths and supported image formats.
- Validate the output file extension.
- Provide clear command-line error messages.

## Requirements

- Python 3.11 or compatible Python version
- `img2pdf`

Install the required dependency with:

    python -m pip install -r requirements.txt

## Usage

### Convert a single image

    python convert_image_to_pdf.py "image.jpg"

The default output file will be:

    output.pdf

### Convert multiple images

Place your JPG/JPEG images inside a folder and run:

    python convert_image_to_pdf.py ./images

### Specify a custom output filename

    python convert_image_to_pdf.py "image.jpg" -o converted.pdf

For a folder:

    python convert_image_to_pdf.py ./images -o combined.pdf

## Supported Formats

The converter currently supports:

- `.jpg`
- `.jpeg`

Other image formats are rejected with a clear error message.

## Command-Line Options

    python convert_image_to_pdf.py [-h] [-o OUTPUT] input

### Arguments

- `input` — Path to a JPG/JPEG image or a folder containing JPG/JPEG images.
- `-o`, `--output` — Output PDF filename. The default is `output.pdf`.
- `-h`, `--help` — Display the help message.

## Error Handling

The program handles common input problems, including:

- Input path does not exist.
- Unsupported image format.
- Folder contains no JPG/JPEG images.
- Output filename does not use the `.pdf` extension.
- Output path points to a directory instead of a file.

## Project Structure

    Image-to-PDF-Converter/
    │
    ├── convert_image_to_pdf.py
    ├── requirements.txt
    ├── README.md
    └── .gitignore

## How It Works

1. The program receives an image or folder path from the command line.
2. It checks whether the input exists and contains supported images.
3. JPG/JPEG files are collected and sorted by filename.
4. `img2pdf` converts the images into a PDF.
5. The generated PDF is saved using the specified output filename.

## Technologies Used

- Python
- argparse
- pathlib
- img2pdf

## Example

    python convert_image_to_pdf.py ./images -o photos.pdf

Example output:

    Successfully converted 3 image(s) to photos.pdf

## Author

**Hrishikesh Sharma**

GitHub: RaavanHrishi07

## License

This project is licensed under the MIT License.    