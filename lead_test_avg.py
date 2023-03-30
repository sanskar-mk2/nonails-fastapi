from PIL import Image, ImageFilter
from tempfile import SpooledTemporaryFile


def get_mean(image: SpooledTemporaryFile):
    gray = Image.open(image).convert("LA")
    avg = gray.filter(ImageFilter.MedianFilter(size=9))
    width, height = avg.size

    total = 0
    for i in range(0, width):
        for j in range(0, height):
            total += avg.getpixel((i, j))[0]

    mean = total / (width * height)
    return mean
