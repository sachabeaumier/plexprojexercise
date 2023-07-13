import math as m
import json
from pathlib import Path


# functions to calculate area of different shape types
def circle_area(radius):
    return m.pi * radius * radius


def rect_area(width, height):
    return width * height


def triangle_area(base, height):
    return 0.5 * base * height


def unknown_shape():
    return 'type of unknown shape'


# main function
def main():
    total_area = []
    file_path = Path('data.jsonl')
    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line)

            if data['type'] == "rectangle":
                width = data['width']
                height = data['height']
                area = rect_area(width, height)
                total_area.append(area)
                print(f"area of rectangle: {area}")
            elif data['type'] == "triangle":
                base = data['base']
                height = data['height']
                area = triangle_area(base, height)
                total_area.append(area)
                print(f"area of a triangle: {area}")
            elif data['type'] == "circle":
                radius = data['radius']
                area = circle_area(radius)
                total_area.append(area)
                print(f"area of circle: {area}")
            else:
                print(unknown_shape())

    array_sum = sum(total_area)
    print(f"total sum of all shape areas in the JSON data is {round(array_sum, 2)}")


main()
