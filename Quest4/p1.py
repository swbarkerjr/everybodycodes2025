def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest4/sample1-1.txt')
    gears = list((int(num.strip('\n')) for num in data))
    ratio = gears[0] / gears[len(gears)-1]
    result = int(ratio * 2025)
    print(result)

def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()
    
if __name__ == '__main__':
    main()