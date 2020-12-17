from PIL import Image
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="Pixelate an image.")
    parser.add_argument(
        "-p",
        "--pixels",
        type=int,
        default=16,
        help="The number of pixels to produce per row or column of the output image.",
    )
    parser.add_argument("-o", "--output", help="The (optional) file to output to.")
    parser.add_argument("image", help="The original image to pixelate.")
    return parser


args = create_parser().parse_args()


with Image.open(args.image) as img:
    small = img.resize((args.pixels, args.pixels), resample=Image.BILINEAR)
    result = small.resize(img.size, Image.NEAREST)
    if args.output:
        result.save(args.output)
    result.show()
