from pathlib import Path
import argparse
import img2pdf


SUPPORTED_EXTENSIONS = {".jpg", ".jpeg"}


def collect_images(input_path):
    """Return supported image files from a file or directory."""
    path = Path(input_path)

    if not path.exists():
        raise FileNotFoundError(f"Input path does not exist: {input_path}")

    if path.is_file():
        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            raise ValueError("Only JPG and JPEG images are supported.")
        return [path]

    images = sorted(
        file
        for file in path.iterdir()
        if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS
    )

    if not images:
        raise ValueError("No JPG or JPEG images were found in the folder.")

    return images


def convert_to_pdf(input_path, output_path):
    """Convert one image or multiple images into a PDF."""
    images = collect_images(input_path)

    output_file = Path(output_path)

    with output_file.open("wb") as pdf_file:
        pdf_file.write(img2pdf.convert([str(image) for image in images]))

    return len(images)


def main():
    parser = argparse.ArgumentParser(
        description="Convert JPG/JPEG images into a PDF file."
    )

    parser.add_argument(
        "input",
        help="Path to a JPG/JPEG image or a folder containing images."
    )

    parser.add_argument(
        "-o",
        "--output",
        default="output.pdf",
        help="Output PDF filename (default: output.pdf)."
    )

    args = parser.parse_args()

    try:
        image_count = convert_to_pdf(args.input, args.output)
        print(f"Successfully converted {image_count} image(s) to {args.output}")

    except (FileNotFoundError, ValueError, OSError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
    