import math
def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest4/part3.txt')
    gears = list(num.strip('\n') for num in data)
    gears = list(num.split('|') for num in gears)

    print(f'Final ratio: {final_ratio(gears)}')
    print(f'output gear turns: {int(100*final_ratio(gears))}')


def final_ratio(gears):
    ratio = int(gears[0][0])
    for item in gears[1:-1]:
        print(item)
        ratio = ratio / int(item[0]) * int(item[1])
    print(gears[-1][0])
    ratio = ratio / int(gears[-1][0])
    return ratio

def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()

if __name__ == '__main__':
    main()