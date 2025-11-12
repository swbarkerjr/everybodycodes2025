def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest1/everybody_codes_e2025_q01_p2.txt')
    potential_names = data[0].split(',')
    print(f'Length of potential_name {len(potential_names)}')
    instructions = data[2]
    position = 1
    for instruction in instructions.split(','):
        move = int(instruction[1:])
        if instruction[0] == 'R':
            if position + move > len(potential_names):
                position = (position + move) % len(potential_names)
            else:
                position += move
        else: 
            if position - move < 1:
                position = len(potential_names) + (position - move)
            else: 
                position -= move
    print(f'Name is {potential_names[position-1]}')

def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()



if __name__ == '__main__':
    main()