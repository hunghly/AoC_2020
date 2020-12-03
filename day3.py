test_input = [\
"..##.......",\
"#...#...#..",\
".#....#..#.",\
"..#.#...#.#",\
".#...##..#.",\
"..#.##.....",\
".#.#.#....#",\
".#........#",\
"#.##...#...",\
"#...##....#",\
".#..#...#.#"]


def travel_path(line, start_pos):
    didHit = "Hit" if line[start_pos] == '#' else "Miss"
    if didHit == "Hit":
        return True
    else:
        return False


if __name__ == '__main__':
    with open('day3.txt', 'r') as file:
        lines = file.readlines()
    # initialize variables
    start_pos = 0
    hit_count = 0
    slope = [3, 1]

    for i in range(
            0, len(lines), slope[1]
    ):  # loop through lines based, skips lines based on slope step
        line = lines[i]
        hit = travel_path(
            line, start_pos %
            (len(line) - 1))  # check to see if there was a tree hit
        if hit:
            hit_count += 1
        start_pos += slope[0]
    print("# of Tree's hit is: ", hit_count)