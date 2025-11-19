def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest8/part2.txt')
    nail_count = 256
    count = 0
    tested_pairs = list()
    
    data = list((int(num) for num in data[0].split(',')))
    pairs = list()
    for x in range(len(data)-1):
        pairs.append([data[x],data[x+1]])
    
    while len(pairs) != len(tested_pairs):
        for x in pairs:
            if len(tested_pairs) == 0:
                tested_pairs.append(x)
                continue
            for y in tested_pairs:
                if abs(x[0]-x[1]) == 1:     # 1 unit segment, can't cross anything
                    break
                elif x[0] in y or x[1] in y:  # shares vertex check
                    continue
                elif middle_crossing(x,y,nail_count):   # midpoint cross check
                    count += 1
                else:
                    # Rotate the circle so the start of test line begins at 1
                    # determine rotation amount.
                    # look at each existing line (adjusted for rotation), are they all on one side of the test line (both start and end numbers > max and < min)? then line does not cross this one, else it does.

                    # rotation = 1 - test_line_start
                    rotation = 1 - x[0]
                    # rotated_test_line_start = 1
                    rotated_x_start = 1
                    # rotated_test_line_end = test_line_end - rotation
                    rotated_x_end = x[1] + rotation           
                    # if negative: abs(mod with nail)
                    if rotated_x_end < 0:
                        rotated_x_end = abs(rotated_x_end % nail_count)
                    # if zero, set to nail count
                    if rotated_x_end == 0:
                        rotated_x_end = nail_count
                    # rotated_existing_line_start and end (= existing_start - rotation)
                    rotated_y_start = y[0] + rotation
                    rotated_y_end = y [1] + rotation
                    # if negative: abs(mod with nail)
                    if rotated_y_start < 0:
                        rotated_y_start = abs(rotated_y_start % nail_count)
                    # if zero, set to nail count
                    if rotated_y_start == 0:
                        rotated_y_start = nail_count
                    if rotated_y_end < 0:
                        rotated_y_end = abs(rotated_y_end % nail_count)
                    # if zero, set to nail count
                    if rotated_y_end == 0:
                        rotated_y_end = nail_count
                    
                    #     check if rotated_start > 1 and rotated_end < rotated_test_end:
                    if rotated_y_start > 1 and rotated_y_start < rotated_x_end and rotated_y_end > 1 and rotated_y_end < rotated_x_end :
                    #         same side, ignore
                        continue
                    elif rotated_y_start > rotated_x_end and rotated_y_end > rotated_x_end:
                    #         same side, ignore
                        continue
                    else:
                        count += 1
                    
                    
            tested_pairs.append(x)
    
    print(f'part2: {count}')

def pos_direction(_x,_nails):
    if max(_x) - min(_x) > _nails/2:
        return True
    return False

def middle_crossing(_pair1:list,_pair2:list, _nails:int) -> bool:
    if abs(_pair1[0]-_pair1[1]) == abs(_pair2[0] - _pair2[1]) and abs(_pair1[0]-_pair1[1]) == _nails/2:
        return True
    return False

def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()
    
if __name__ == '__main__':
    main()
