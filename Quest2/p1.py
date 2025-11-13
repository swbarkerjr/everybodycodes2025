def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest2/everybody_codes_e2025_q02_p1.txt')
    X = int(data[0].split('=')[1].split(',')[0][1:])
    Y = int(data[0].split('=')[1].split(',')[1][:-1])
    A = [X,Y]
    
    R = [0,0]

    for i in range(3):
        R = mult(R,R)
        R = div(R,[10,10])
        R = add(R, A)
    
    print(f'Result is {R}')

def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()

def add(x: list,y: list) -> list:
    #[X1,Y1] + [X2,Y2] = [X1 + X2, Y1 + Y2]
    return [int(x[0])+int(y[0]),int(x[1])+int(y[1])]

def mult(x: list, y: list) -> list:
    #[X1,Y1] * [X2,Y2] = [X1 * X2 - Y1 * Y2, X1 * Y2 + Y1 * X2]
    return [int(x[0]) * int(y[0]) - int(x[1]) * int(y[1]), int(x[0]) * int(y[1]) + int(x[1]) * int(y[0])]
    
def div(x: list, y: list) -> list:
    #[X1,Y1] / [X2,Y2] = [X1 / X2, Y1 / Y2] - ignore remainder
    return [int(x[0]) // int(y[0]), int(x[1]) // int(y[1])]
    


if __name__ == '__main__':
    main()