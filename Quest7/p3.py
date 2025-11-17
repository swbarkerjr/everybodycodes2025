def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest7/part3.txt')
    names = data[0].strip('\n').split(',')
    rules_dict = create_dict(list(item.strip('\n') for item in data[2:]))
    valid_name_count = 0

    unique_prefix_list = find_unique_prefix(names)

    for prefix in unique_prefix_list:
        if validate_name(prefix, rules_dict):
            valid_name_count += build_names(prefix,rules_dict, 0)
            
    print(f'part3: {valid_name_count}')

def build_names(_prefix: str, _rules_dict: list, _count: int):
    if _prefix[-1] in _rules_dict.keys():
        for char in _rules_dict[_prefix[-1]]:
            new_name = _prefix+char
            if len(new_name) >= 7:
               # print(new_name)
                _count += 1
            if len(new_name) < 11:
               _count = build_names(new_name,_rules_dict, _count)
        
    return _count
   
def find_unique_prefix(_prefix_list: list):
    items_to_remove = list()
    _sorted_prefix_list = sorted(_prefix_list, key=len)
    for index, prefix in enumerate(_sorted_prefix_list):
        for item in _sorted_prefix_list[index+1:]:
            if prefix in item:
                items_to_remove.append(item)
    for item in items_to_remove:
        try:
            _prefix_list.remove(item)
        except:
            pass
    return _prefix_list

def validate_name(name,rules_dict):
    for x in range(len(name)-1):
        if name[x+1] not in list(rules_dict.get(name[x])):
            return False
    return True


def create_dict(rules):
    rule_dict = dict()
    for rule in rules:
        rule = rule.split('>')
        rule_dict[rule[0].strip()] = list(rule[1].strip().split(','))
    return rule_dict


def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()
    
if __name__ == '__main__':
    main()

