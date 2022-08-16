from typing import List


def stone_wall(wall: str) -> int:
    empty = [0] * 10
    i = 0
    for stone in wall:
        # print(stone)
        if stone == " ":
            i = -1
        elif stone == "0":
            empty[i] += 1
        i += 1
    return empty.index(max(empty))

if __name__ == "__main__":
    assert (stone_wall('''##########
                          ####0##0##
                          00##0###00''') == 4)
    assert (stone_wall('''#########0
                          ####0##0#0
                          00##0###00''') == 9)
    assert (stone_wall('''####
                          ####
                          ####''') == 0)
    assert (stone_wall('''###0
                          #0#0
                          #0##''') == 1)
    assert (stone_wall('''###00
                          #0#00
                          #0##0''') == 4)
    assert (stone_wall('''###00
                          #0#00
                          #0#00''') == 3)
    assert (stone_wall('''#0#00
                          #0#00
                          #0#00
                          0####
                          0####''') == 1)
    assert (stone_wall("""#0#
    ###
    ###""") == 1)