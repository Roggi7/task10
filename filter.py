from PIL import Image
import numpy as np


def create_color(img_list, i, j, gray_sum, area, step):
    """
    Принимает на вход пиксельную матрицу изображения,
    Индексы текущего пикселя,
    Размер блока и количество градаций серого,
    Возвращая новую цветовую гамму для заданного размера матрицы.
    """
    for x in range(i, i + area):
        for y in range(j, j + area):
            for z in range(3):
                img_list[x][y][z] = int(gray_sum // step) * step


def Create_IMG(img, out, area, step):
    """
    Принимает на вход исходное изображение, название преображенного файла,
    Размер блока и количество градаций серого,
    Возвращает преобразованное изображение.
    >>> Create_IMG("img.jpg", "res.jpg", 10, 50)
    """
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


Create_IMG(input("name:"),
           input("out_name:"),
           int(input("area:")),
           int(input("step:")))
