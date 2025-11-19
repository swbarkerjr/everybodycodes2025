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
                if abs(x[0]-x[1]) == 1:     #1 unit segment, can't cross anything
                    break
                elif x[0] in y or x[1] in y:  #shares vertex
                    continue
                elif middle_crossing(x,y,nail_count):
                    count += 1
                else:
                    #find numbers between ends of x on shortest distance around circle
                    if pos_direction(x,nail_count):
                        next = max(x)
                        while next != min(x):
                            next += 1           #cycle positive (clockwise)
                            if next > nail_count:
                                next = next % nail_count
                            if next in y:
                                count += 1
                                break
                    else:
                        next = max(x)
                        while next != min(x):
                            next -= 1
                            if next in y:
                                count += 1
                                break

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
