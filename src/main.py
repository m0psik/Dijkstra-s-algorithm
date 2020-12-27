from Dungeon import Dungeon
import re
import sys


def parse(inputStream):
    dungeon = Dungeon()
    start_point = None
    end_point = None
    for line in inputStream:
        if line == '\n':
            continue
        line = line.replace('\n', '')

        # parse start_point and end_point
        if re.match(r'^\S+ \S+$', line) and start_point is None and end_point is None:
            start_point, end_point = line.split()

        # parse edge with type
        elif re.match(r'^\S+ \S+ \d+ [ud]$', line) and start_point is not None and end_point is not None:
            start, end, dist, edge_type = line.split()
            try:
                dungeon.add_edge(start, end, int(dist), edge_type)
            except Exception as msg:
                return dungeon, start_point, end_point, msg

        # parse edge without type (by default, the edge is oriented)
        elif re.match(r'^\S+ \S+ \d+$', line) and start_point is not None and end_point is not None:
            start, end, dist = line.split()
            try:
                dungeon.add_edge(start, end, int(dist))
            except Exception as msg:
                return dungeon, start_point, end_point, msg

        else:
            return dungeon, start_point, end_point, 'Invalid input'

    if start_point is None or end_point is None:
        return dungeon, start_point, end_point, 'Invalid input'

    return dungeon, start_point, end_point, None


if __name__ == '__main__':
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    with open(input_path) as file_in:
        dungeon_, start_point_, end_point_, error = parse(file_in)

    if error is None:
        answer, err = dungeon_.find_way(start_point_, end_point_)
        if err is not None:
            answer = [err]
    else:
        answer = [error]

    with open(output_path, 'w') as file_out:
        print(*answer, file=file_out, sep='\n')
