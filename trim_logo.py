from PIL import Image, ImageChops
import os

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im

try:
    img_path = "images/logo.png"
    if os.path.exists(img_path):
        im = Image.open(img_path)
        im = trim(im)
        im.save(img_path)
        print(f"Successfully trimmed {img_path}")
    else:
        print(f"File not found: {img_path}")
except Exception as e:
    print(f"Error: {e}")
