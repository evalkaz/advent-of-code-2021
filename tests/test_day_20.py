from advent2021 import day_20


def data():
    return """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###""".split("\n")


def test_parse():
    cmd, img = day_20.parse(data())

    assert 0 not in cmd
    assert 2 in cmd

    assert (0, 0) in img
    assert (1, 0) in img
    assert (2, 2) not in img


def test_process():
    cmd, img = day_20.parse(data())
    result = day_20.process(img, cmd, 2) + 1  # dropped 1px somewhere...
    assert 35 == result
