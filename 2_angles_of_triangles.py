from math import acos, degrees
from typing import List


def calculate_angles(a: int, b: int, c: int) -> List[int]:
    angle_a, angle_b, angle_c = 0, 0, 0
    if a + b > c and a + c > b and c + b > a:
        angle_a = round(degrees(acos((b**2 + c**2 - a**2)/(2 * b * c))))
        angle_b = round(degrees(acos((a**2 + c**2 - b**2)/(2 * a * c))))
        angle_c = round(degrees(acos((a**2 + b**2 - c**2)/(2 * a * b))))
    angles = [angle_a, angle_b, angle_c]
    angles.sort()
    return angles
    
    
if __name__ == "__main__":
    assert(calculate_angles(4, 4, 4) == [60, 60, 60])
    assert(calculate_angles(3, 4, 5) == [37, 53, 90])
    assert(calculate_angles(2, 2, 5) == [0, 0, 0])
