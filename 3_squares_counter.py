from typing import List


def h_line_exist(edges: List[List[int]], a: int, b: int) -> bool:
    for i in range(a, b):
        if [i, i + 1] not in edges and [i + 1, i] not in edges:
            return False
    return True


def v_line_exist(edges: List[List[int]], a: int, b: int):
    for i in range(a, b, 4):
        if [i, i + 4] not in edges and [i + 4, i] not in edges:
            return False
    return True

def is_square(edges: List[List[int]], num: int, size: int) -> bool:
    if h_line_exist(edges, num, num + size) and \
            h_line_exist(edges, num + 4 * size, num + size + 4 * size) and \
            v_line_exist(edges, num + size, num + size + 4 * size) and \
            v_line_exist(edges, num, num + 4 * size):
        return True
    return False


def check_squares(edges: List[List[int]], i: int, j: int) -> int:
    num = i * 4 + j + 1
    square_count = 0
    for size in range(1, min(4 - j, 4 - i)):
        square_count += is_square(edges, num, size)
    
    return square_count


def number_of_squares(edges: List[List[int]]) -> int:
    square_count = 0
    for i in range(4):
        for j in range(4):
            square_count += check_squares(edges, i, j)
    return square_count


if __name__ == "__main__":
    assert(number_of_squares([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                               [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                               [10, 14], [12, 16], [14, 15], [15, 16]]) == 3)
    
    assert(number_of_squares([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                               [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                               [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2)
    
    assert(number_of_squares([[1, 2]]) == 0)

    assert (number_of_squares([[]]) == 0)
    
    assert(number_of_squares([[5, 6], [6, 7], [7, 11], [11, 15], [15, 14], [13, 14], [13, 9], [9, 5]]) == 1)
    
    assert(number_of_squares([[7, 8], [8, 12], [12, 11], [11, 7]]) == 1)
    
    assert(number_of_squares([[1, 2], [2, 3], [3, 4], [4, 8], [8, 12], [12, 16], [1, 5], [5, 9], [9, 13], [2, 6],
                              [6, 10], [10, 11], [12, 11], [7, 3], [7, 8], [13, 14], [14, 15], [16, 15]]) == 3)
    
    assert (number_of_squares([[1, 2], [2, 3], [3, 4], [4, 8], [8, 12], [12, 16], [1, 5], [5, 9], [9, 13], [2, 6],
                               [6, 10], [10, 11], [12, 11], [7, 3], [7, 8], [13, 14], [14, 15], [16, 15], [7, 11]]) == 4)