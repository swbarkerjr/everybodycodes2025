def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest8/part1.txt')
    data = list((int(num) for num in data[0].split(',')))
    count = 0
    nail_count = 32
    for x in range(len(data)-1):
        if middle_crossing(data[x:x+2], nail_count):
            count += 1
    print(f'part1: {count}')


def middle_crossing(_pair:list,_nails:int) -> bool:
    if abs(_pair[0]-_pair[1]) == _nails/2:
        return True
    return False

def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()
    
if __name__ == '__main__':
    main()

