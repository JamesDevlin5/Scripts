from PIL import Image, ImageDraw
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description="Create a picture that is the horizontal average color of each pixel."
    )
    parser.add_argument("image", help="The image to create an average composite of.")
    return parser


def avg(list):
    return int(sum(list) / len(list))


args = create_parser().parse_args()

with Image.open(args.image) as img:
    draw = ImageDraw.Draw(img)
    for x in range(img.width):
        r, g, b = [], [], []
        for y in range(img.height):
            pixel = img.getpixel((x, y))
            r.append(pixel[0])
            g.append(pixel[1])
            b.append(pixel[2])
        avg_r = avg(r)
        avg_g = avg(g)
        avg_b = avg(b)
        draw.rectangle((x, 0, x, img.height), fill=(avg_r, avg_g, avg_b))
    img.show()
