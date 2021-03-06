from PIL import Image
import numpy as np


def create_color(img_list, i, j, gray_sum, area, step):
    for x in range(i, i + area):
        for y in range(j, j + area):
            for z in range(3):
                img_list[x][y][z] = int(gray_sum // step) * step


def create_img(img, out, area, step):
    img_list = np.array(Image.open(img))
    pixels_count = len(img_list)
    width = len(img_list[1])
    i = 0
    while i < pixels_count - 9:
        j = 0
        while j < width - 9:
            section = img_list[i: area + i, j: area + j]
            gray_sum = int(np.sum(section) // (area ** 2)) / 3
            create_color(img_list, i, j, gray_sum, area, step)
            j += 10
        i += 10
    Image.fromarray(img_list).save(out)


create_img('img.jpg', 'res.jpg', 10, 50)
