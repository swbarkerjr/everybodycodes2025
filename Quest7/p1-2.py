def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest7/part2.txt')
    names = data[0].strip('\n').split(',')
    rules_dict = create_dict(list(item.strip('\n') for item in data[2:]))
    count = 0
    for index, name in enumerate(names):
        if validate_name(name, rules_dict):
            count += index + 1
            print(index, name)
    print(count)


def validate_name(name,rules_dict):
    for x in range(len(name)-1):
        if name[x+1] not in list(rules_dict.get(name[x])):
            return False
    return True


def create_dict(rules):
    rule_dict = dict()
    for rule in rules:
        rule = rule.split('>')
        rule_dict[rule[0].strip()] = rule[1].strip()    
    return rule_dict


def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()
    
if __name__ == '__main__':
    main()

