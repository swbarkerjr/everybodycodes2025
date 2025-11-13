def main():
    count = 0
    point_count = 0
    grid_size = 1000
    divisions = 100
    step = int(grid_size/divisions)

    data = readfile('/home/steve/everybodycodes/2025/Quest2/everybody_codes_e2025_q02_p2.txt')
    X1 = int(data[0].split('=')[1].split(',')[0][1:])
    Y1 = int(data[0].split('=')[1].split(',')[1][:-1])
    P = [X1,Y1]

    for x in range(X1, X1+grid_size+step, step):
        for y in range(Y1, Y1+grid_size+step, step):
            RX1, RY1 = 0, 0
            point_count += 1
            for i in range(100):
                RX1, RY1 = mult(RX1, RY1, RX1, RY1)
                RX1, RY1 = div(RX1, RY1, 100000, 100000)
                RX1, RY1 = add(RX1, RY1, x, y)
                if abs(RX1)>1000000 or abs(RY1)>1000000:
                    break
                if i == 99:
                    count += 1
    print(f'count = {count}')              


def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()

def add(X1: int,Y1: int, X2: int, Y2: int) -> int:
    #[X1,Y1] + [X2,Y2] = [X1 + X2, Y1 + Y2]
    return X1 + X2, Y1 + Y2

def mult(X1: int,Y1: int, X2: int, Y2: int) -> int:
    #[X1,Y1] * [X2,Y2] = [X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2]
    return X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2
    
def div(X1: int,Y1: int, X2: int, Y2: int) -> int:
    #[X1,Y1] / [X2,Y2] = [X1 / X2, Y1 / Y2] - ignore remainder
    return int(X1 / X2), int(Y1 / Y2)

if __name__ == '__main__':
    main()