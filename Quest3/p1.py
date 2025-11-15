def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest3/data-q03-pt1.txt')
    data = list(int(num) for num in data[0].split(','))
    data.sort(reverse=True)
    set = list()
    current_value = data[0]
    sum = current_value
    set.append(current_value)
    for num in data:
        if num < current_value:
            current_value = num
            sum += current_value
            set.append(current_value)
    print(set,sum)


def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()
    


if __name__ == '__main__':
    main()