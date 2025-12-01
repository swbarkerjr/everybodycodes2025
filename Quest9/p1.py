def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest9/part1.txt')
    dna_seq = list()
    for item in data:
        dna_seq.append(item.strip('\n').split(':'))
    
    child, similarity_number = find_degree_of_similarity([dna_seq[0],dna_seq[1],dna_seq[2]])
    if child != 0:
        print(f'part1: child: {child}, degree of similarity: {similarity_number}')
    else:
        print(f'No child found')


#function to determine which of 3 inputs ['C', 'C', 'T'] can be a child. Indices 0 or 1 in this example
def child_check(_input: list) -> list:
    if _input[0] == _input[1] == _input[2]: return [0,1,2]
    if _input[0] == _input[1]: return [0,1]
    if _input[1] == _input[2]: return [1,2]
    if _input[0] == _input[2]: return [0,2]
    return None

#function to compare list of 3 dna characters [G,G,T] and return list of potential children
def possible_children(_dna_list:list, _children:list) -> list:
    _new_potential_children = list()
    _potential_child = child_check(_dna_list)
    if _potential_child:
        for item in _potential_child:
            if item in _children:
                _new_potential_children.append(item)
        if len(_new_potential_children) == 0:
            return None
    return _new_potential_children

def find_degree_of_similarity(dna_list: list) -> list:
    #compairs sequence of 3 items and returns the child number and similarity calculation
    #dna_list input is of format child#:DNA_sequence [23:GATCCCTGATGAAC....]
    match_count = [0,0,0]
    found_child = False
    children = [0,1,2]
    child_index = int()
    for i in range(len(dna_list[0][1])):
        test_dna = [dna_list[0][1][i], dna_list[1][1][i], dna_list[2][1][i]]
        children = possible_children(test_dna, children)
        if children:
            if dna_list[0][1][i] == dna_list[1][1][i] or dna_list[0][1][i] == dna_list[2][1][i]: 
                match_count[0] += 1
            if dna_list[1][1][i] == dna_list[0][1][i] or dna_list[1][1][i] == dna_list[2][1][i]: 
                match_count[1] += 1
            if dna_list[2][1][i] == dna_list[0][1][i] or dna_list[2][1][i] == dna_list[1][1][i]: 
                match_count[2] += 1
        
            if not found_child and match_count.count(max(match_count)) == 1:
                child_index = match_count.index(max(match_count))
                found_child = True
        else:
            return [0,0]        
    if found_child:
        del match_count[child_index]
        return [dna_list[child_index][0], match_count[0] * match_count[1]]
    return [0,0]

def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()
    
if __name__ == '__main__':
    main()


