def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest6/part3.txt')
    people = data[0]
    multiplier = 1000
    distance = 1000
    part3_count = 0

    A=find_mentor_app_count(people,'A', 'a')
    B=find_mentor_app_count(people,'B', 'b')
    C=find_mentor_app_count(people,'C', 'c')
    print(f'A: {A}')
    print(f'B: {B}')
    print(f'C: {C}')
    print(A+B+C)

    all_people = multiply_people(people,multiplier)
    for index,apprintice in enumerate(all_people):
        if apprintice in ['a', 'b', 'c']:
            #print(f'segment: {segment(all_people,index,distance)}')
            part3_count += find_mentor_count(segment(all_people,index,distance), apprintice.upper())
            #print(find_mentor_count(segment(all_people,index,distance), apprintice.upper()))
    print(f'Part 3 count: {part3_count}')

def find_mentor_app_count(people, mentor, apprentice):
    count = 0
    for index, knight in enumerate(people):
        if knight == mentor:
            for x in range(index+1, len(people)):
                if people[x] == apprentice:
                    count += 1
    return count

def find_mentor_count(people, mentor):
    return people.count(mentor)

def multiply_people(people,multiplier):
    return people *multiplier
    

def segment(people, index, distance):
    if index < distance:
        return people[:index+distance+1]
    if index > len(people) - distance:
        return people[index-distance:]
    else:
        return people[index-distance:index+distance+1]


def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()
    
if __name__ == '__main__':
    main()

