from p1 import find_degree_of_similarity

def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest9/part2.txt')
    dna_seq = list()
    total = 0
    for item in data:
        dna_seq.append(item.strip('\n').split(':'))  
    print(f'part2: total = {scan_dna_sequences(dna_seq)}')

def scan_dna_sequences(dna_seq):
    children = list()
    child, total, similarity_number = 0, 0, 0
    for index1, dna1 in enumerate(dna_seq[:-2]):
        for index2, dna2 in enumerate(dna_seq[index1+1:-1]):
            for index3, dna3 in enumerate(dna_seq[index1+2:]):
                #if child_possible_check([dna1,dna2,dna3]):
                child, similarity_number = find_degree_of_similarity([dna1,dna2,dna3])
                if child !=0 and child not in children:
                    total += similarity_number
                    children.append(child)
                    print(f'part2: child: {child}, degree of similarity: {similarity_number}')
    return total


def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()
    
if __name__ == '__main__':
    main()

