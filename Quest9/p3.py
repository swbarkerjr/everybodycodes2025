from p1 import find_degree_of_similarity

def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest9/part3.txt')
    dna_seq = list()
    total = 0
    for item in data:
        dna_seq.append(item.strip('\n').split(':'))
    child, child_parents = scan_dna_sequences(dna_seq)
   # print(f'child/parents: {child_parents}')
   # print(f'parents {child_parents.values()}')
    
    #scan child_parent dict and gather parents into list of parents (tuples).  [(1,2),(5,6)]
    parent_list = []
    for item in child_parents.values():
        if item not in parent_list:
            parent_list.append(item)
   # print(f'parent_list: {parent_list}')

   #gather children from same parents in child_parent dict into a dict of parents_child. 2 parents, 1 or more children {(1,2):[3], (4,5): [7,6]}
    parent_child = dict()
    for item in parent_list:
        parent_child[item] = []
        for key, value in child_parents.items():
            if item == value:
                parent_child[item].append(key)
   # print(f'parents/children: {parent_child}')

   #create family_units list by gathering parents and children from parent_child dict into a list of units [[3,1,2], [7,6,4.5]]
    family_units = []
    #for index, item in enumerate(parent_list):
    extended_families = []
    for parents, children in parent_child.items():
        #children = list(child for child in value)
        temp = list()
        found_family = False
        temp.append(parents[0])
        temp.append(parents[1])
        temp.append(children[0])

        if len(extended_families) == 0:
            extended_families.append(temp)
            continue

        for ext_fam in extended_families:
            if children[0] in ext_fam:
                for num in temp:
                    ext_fam.append(num)
                found_family = True
                continue
            if parents[0] in ext_fam:
                for num in temp:
                    ext_fam.append(num)
                found_family = True
                continue
            if parents[1] in ext_fam:
                for num in temp:
                    ext_fam.append(num)
                found_family = True
                continue
        if not found_family:
            extended_families.append(temp)

    max_family_size = 0
    for family in extended_families:
        family_size = sum(list(set(family)))
        
        if family_size > max_family_size:
            max_family_size = family_size

   # print(f'family units {family_units}')

    # max_family_size = 0
    # for index, family in enumerate(family_units):
    #     current_family_size = find_extended_family(family, family_units[index+1:])
    #     if current_family_size > max_family_size:
    #         max_family_size = current_family_size
    print(f'max family size = {max_family_size}')



def find_extended_family(_family,_remaining_families):
    #for index, family in enumerate(_family_units):
    family_size = sum(_family)
    if len(_remaining_families) == 0:
        return family_size
    for item in _family:
        for index, next_family in enumerate(_remaining_families):
            if item in next_family and next_family != _family:
                
                family_size -= item     #remove the duplicate family member - only count once
                family_size += find_extended_family(next_family, _remaining_families)

    return family_size
        


def scan_dna_sequences(dna_seq):
    parents = dict()
    child, total, similarity_number = 0, 0, 0
    for index1, dna1 in enumerate(dna_seq[:-2]):
        for index2, dna2 in enumerate(dna_seq[index1+1:-1]):
            for index3, dna3 in enumerate(dna_seq[index1+2:]):
                #if child_possible_check([dna1,dna2,dna3]):
                child, similarity_number = find_degree_of_similarity([dna1,dna2,dna3])
                if child !=0 and int(child) not in parents.keys():
                    total += similarity_number
                    parents[int(child)] = ()
                    for item in [dna1,dna2,dna3]:
                        if child != item[0]:
                            parents[int(child)] = parents[int(child)] + (int(item[0]),)
                    #print(f'part2: child: {child}, degree of similarity: {similarity_number}')
    return total, parents


def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()
    


if __name__ == '__main__':
    main()