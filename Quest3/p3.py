def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest3/data-q03-pt3.txt')
    data = list(int(num) for num in data[0].split(','))
    data.sort()
    set_count = 0
    while data:
        set = list()
        current_value = data[0]
        sum = current_value
        set.append(current_value)
        for num in data:
            if num > current_value:
                current_value = num
                sum += current_value
                set.append(current_value)
        set_count += 1
        print(set,sum, set_count)
        for item in set:
            data.remove(item)

def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()
    


if __name__ == '__main__':
    main()