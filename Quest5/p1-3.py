def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest5/part3.txt')
    swords = list()
    for sword in data:
        swords.append(analyze_sword(sword))
    swords = convert_children_to_num(swords)
    swords = sorted(swords, key=lambda x: x[1], reverse=True)
    
    switched = True
    count = 1
    while count != len(swords[0]):
        for index in range(len(swords)-1):
            switched = False
            if swords[index][1] == swords[index+1][1]:
                switched = sort_2_lists_by_rules(swords[index], swords[index+1])
            if switched:
                swords[index], swords[index+1] = swords[index+1], swords[index]
        count += 1
    

    for sword in swords:
        print(sword, len(sword))
    print(f'Part1: quaility : {swords[0][1]}')
    print(f'Part2: max/min quaility difference: {diff(swords)}')
    print(f'Part3: total checksum: {checksum_calc(swords)}')

def checksum_calc(data):
    total = 0
    for i in range(len(data)):
        total += (i+1) * data[i][0]
    return total

def sort_2_lists_by_rules(item1: list, item2: list):
    for index in range(2,len(item2)):   
        if item1[index] == item2[index]: 
            continue
        if item1[index] > item2[index]: 
            return False
        if item1[index] < item2[index]:
            return True
    if item1[0] < item2[0]:
        return True



def convert_children_to_num(data):
    updated_data = []
    for indexa, item in enumerate(data):
        updated_data.append(list(item[:2]))
        for child in item[2]:
            temp = list()
            try:
                temp.append(child[1][0])
            except:
                pass
            temp.append(child[0])
            try:
                temp.append(child[1][1])
            except:
                pass
            temp.sort()
            temp_string = ''
            for x in temp:
                temp_string += str(x)
            updated_data[indexa].append(int(temp_string))
    return updated_data

def analyze_sword(data):
    data = data.split(',')
    sword_id, data[0] = data[0].split(':')
    fishbone = [[int(data[0]),[]]]   #populate first spline entry and empty child list
    for num in data[1:]:
        num = int(num)
        fishbone = create_fishbone(fishbone,num)
    return [int(sword_id),int(sword_quality(fishbone)),fishbone]

def sword_quality(fishbone):
    quality = ''
    for item in fishbone:
        quality = quality + str(item[0])
    return quality

def create_fishbone(fishbone,num):
    for index, spline in enumerate(fishbone):
        children = spline[1]
        if len(children) == 0 and num != spline[0]:   #automatically add if child list empty
            fishbone[index][1].append(num)
            break
        elif len(children) == 2:
            if index + 1 < len(fishbone):
                continue
            else:
                fishbone.append([num,[]])
                break
        elif num > spline[0] and spline[0] > children[0]:
            fishbone[index][1].append(num)
            fishbone[index][1].sort()
            break
        elif num < spline[0] and spline[0] < children[0]:
            fishbone[index][1].append(num)
            fishbone[index][1].sort()
            break
        elif index + 1 == len(fishbone):
            fishbone.append([num,[]])
            break
    return fishbone
        
    
def diff(swords):
    worst = swords[0][1]
    best = swords[0][1]
    for item in swords:
        if item[1] < worst: worst = item[1]
        if item[1] > best: best = item[1]
    return best-worst



def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()
    
if __name__ == '__main__':
    main()

    #correct answer part 1: 2782784532
    #correct answer part 2: 8637361015798
    #correct answer part 3: 31574813