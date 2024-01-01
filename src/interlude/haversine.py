from math import radians
from math import sin
from math import cos
from math import sqrt
from math import asin
import time
import json

EARTH_RADIUS_KM = 6371


def haversine_of_degrees(x0, y0, x1, y1, r: int) -> float:
    dx = radians(x1 - x0)
    dy = radians(y1 - y0)

    y0 = radians(y0)
    y1 = radians(y1)

    root_term = sin(dy / 2)**2 + cos(y0) * cos(y1) * sin(dx / 2)**2
    result = 2 * r * asin(sqrt(root_term))

    return result


def main() -> None:
    json_file = open('data_10000000_flex.json')

    start_time = time.time()
    json_input = json.load(json_file)
    mid_time = time.time()

    total = 0
    count = 0

    for pair in json_input["pairs"]:
        total += haversine_of_degrees(
            pair['x0'],
            pair['y0'],
            pair['x1'],
            pair['y1'],
            EARTH_RADIUS_KM,
        )
        count += 1

    average = total / count
    end_time = time.time()

    print(f"result: {average}")
    print(f"input = {mid_time - start_time} seconds")
    print(f"math = {end_time - mid_time} seconds")
    print(f"total = {end_time - start_time} seconds")
    print(f"throughput = {count / (end_time - start_time)} haversines/s")


if __name__ == '__main__':
    main()
