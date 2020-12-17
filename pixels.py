from PIL import Image
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="Image information.")
    parser.add_argument("image", help="The image to obtain information concerning.")
    return parser


def avg(list):
    return sum(list) / len(list)


args = create_parser().parse_args()
with Image.open(args.image) as im:
    print(f"{im.filename}")
    print(f"w: {im.width}px, h: {im.height}px")
    r, b, g = [], [], []
    for x in range(im.width):
        for y in range(im.height):
            px = im.getpixel((x, y))
            r.append(px[0])
            g.append(px[1])
            b.append(px[2])
    avg_r = avg(r)
    avg_g = avg(g)
    avg_b = avg(b)
    print(f"avg r: {avg_r}\navg g: {avg_g}\navg b: {avg_b}")
