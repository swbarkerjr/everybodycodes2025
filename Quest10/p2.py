import copy

def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest10/pt2.txt')
    valid_moves = [[-2,-1],[-1,-2], [1,-2], [2,-1], [2,1], [1,2],[-1,2],[-2,1]]
    board = []
    move_count = 20
    count = 0
    for item in data:
        board.append(list(item.strip('\n')))
    board_dimensions = [len(board[0]),len(board)]

    start_loc = find_starting_location(board)
    if start_loc == [-1,-1]:
        print(f'Cannot find "D" on board')

    sheep_map = gen_map(board, 'S')
    hide_map = gen_map(board, '#')

    dragon_map = []
    #create blank dragon map
    for row in range(board_dimensions[1]):
        dragon_map.append(['.'] * board_dimensions[0])
    #seed dragon_map with start location
    dragon_map[start_loc[0]][start_loc[1]] = 'X'

    #loop through number of moves in 'move_count' variable
    #no sheep in initial start_loc so starting loop a move 1
    for i in range(1, move_count + 1):
        dragon_map = make_dragon_map(board_dimensions,start_loc,dragon_map,valid_moves)
        
        count += count_sheep(sheep_map,dragon_map,hide_map)
        #print(f'total sheep within range (move {i}) = {count}')
        sheep_map = move_sheep(sheep_map, dragon_map, hide_map)
        count += count_sheep(sheep_map,dragon_map,hide_map)
       # print(f'total sheep within range (move {i}) = {count}')    
        print(f'Sheep eaten in round {i} = {count}')
    
    print(f'Total sheep eaten = {count}')

def move_sheep(_sheep_map:list, _dragon_map:list, _hide_map: list):
    #create blank first row in new sheep_map
    _temp = [['.'] * len(_sheep_map)]
    #add current sheep map except last row to move sheep down 1 row
    _new_sheep_map = _temp + _sheep_map[:-1]
    return _new_sheep_map

def count_sheep(_sheep_map: list, _dragon_map: list, _hide_map: list) -> int:
    _sheep_count = 0
    for y, row in enumerate(_sheep_map):
        for x, col in enumerate(row):
            if col == 'S' and _dragon_map[y][x] == 'X' and _hide_map[y][x] != '#':
                _sheep_count += 1
                #remove eaten sheep from sheep map
                _sheep_map[y][x] = '.'
    return _sheep_count
    

def find_starting_location(_board:list) -> list:
    for y,line in enumerate(_board):
        if 'D' in line:
            x = line.index('D')
            return [x,y]
    return [-1,-1]

def gen_map(_board: list, _char: str) -> list:
    _temp = []
    #create blank move map
    for row in range(len(_board)):
        _temp.append(['.'] * len(_board[0]))
    
    for y, row in enumerate(_board):
        for x, col in enumerate(row):
            if col == _char:
                _temp[y][x] = _char

    return _temp


def make_dragon_map(_board_dimensions:list, _start_loc:list, _move_map: int, _valid_moves: list) -> list:
    
    #scan _move_map for 'X' and add valid_moves
    _temp_map = copy.deepcopy(_move_map)
    for y, row in enumerate(_move_map):
        for x, col in enumerate(row):
            if col == 'X':
                for next_move in _valid_moves:
                    next_x = next_move[0] + x
                    next_y = next_move[1] + y
                    if next_x < 0 or next_x >= _board_dimensions[0] or next_y < 0 or next_y >= _board_dimensions[1]:
                        continue
                    else:
                        _temp_map[next_x][next_y] = 'X'
    
            
    for y, row in enumerate(_temp_map):
        for x, col in enumerate(row):
            if _move_map[x][y] == 'X':
                #remove dragon from old position
                _temp_map[x][y] = '.'
    return _temp_map


def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()
    
if __name__ == '__main__':
    main()


