import math
def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest4/part2.txt')
    gears = list((int(num.strip('\n')) for num in data))
    ratio = gears[0] / gears[len(gears)-1]

    print(f'Final ratio: {ratio}')
    print(f'input gear turns: {math.ceil(10000000000000/ratio)}')

def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()

if __name__ == '__main__':
    main()