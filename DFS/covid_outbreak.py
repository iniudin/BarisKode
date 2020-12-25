import pprint
import time

pp = pprint.PrettyPrinter(indent=4)


def headline(text, /, border="♦", *, width=50):
    print(f" {text} ".center(width, border))


def covid_outbreak(matrix):
    count = 0
    infected = get_rows(matrix, 1)
    if not infected:
        return -1

    healty = get_rows(matrix, 0)
    while healty:
        time.sleep(2)

        spreading(matrix, infected)

        healty = get_rows(matrix, 0)
        infected = get_rows(matrix, 1)

        count += 1
        headline(f"Hari ke {count}")
        pp.pprint(matrix)
    return count


def spreading(matrix, infected):
    h = len(matrix)
    w = len(matrix[0])
    for infect in infected:
        for adjacent in adjacents(infect, h, w):
            matrix[adjacent[0]][adjacent[1]] = 1


def adjacents(infect, h, w):
    x = infect[0]
    y = infect[1]
    """
            0
            ↑
        0 ← 1 → 0
            ↓
            0
    """
    res = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]

    def valid(pos):
        return pos[0] >= 0 and pos[0] < h and pos[1] >= 0 and pos[1] < w

    return list(filter(valid, res))


def get_rows(matrix, val):
    h = len(matrix)
    w = len(matrix[0])
    res = []
    for i in range(0, h):
        for j in range(0, w):
            if matrix[i][j] == val:
                res.append((i, j))
    return res


def main():
    graph = [
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    headline("Hari ke 0")
    pp.pprint(graph)
    print(
        "Semua orang terinfeksi dalam waktu {day} hari.".format(
            day=covid_outbreak(graph)
        )
    )


if __name__ == "__main__":
    main()
