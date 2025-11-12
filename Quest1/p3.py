def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest1/everybody_codes_e2025_q01_p3.txt')
    potential_names = data[0].split(',')
    print(f'Length of potential_name {len(potential_names)}')
    instructions = data[2]
 
    for instruction in instructions.split(','):
        position = 1
        move = int(instruction[1:]) % len(potential_names)
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
        top_name = potential_names[0]
        new_top = potential_names[position-1]
        potential_names[0]=new_top
        potential_names[position-1]=top_name
    print(f'Name is {potential_names[0]}')

def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()



if __name__ == '__main__':
    main()