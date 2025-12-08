import copy
def main():
    part1 = False
    part2 = False
    part3 = True

#part 1
    if part1:
        data = readfile('/home/steve/everybodycodes/2025/Quest12/input1.txt')    
        #set start barrel
        queue = [[0,0]]
        total, explored = explode_barrels(queue,data)
        total += 1  #include count of start barrel(s)
        print(f'part 1 total = {total}')

#part 2
    if part2:
        data = readfile('/home/steve/everybodycodes/2025/Quest12/input2.txt')
        #set start barrels
        queue = [[0,0],[len(data)-1,len(data[0])-1]]
        total, explored = explode_barrels(queue,data)
        total += 2   #include count of start barrel(s)
        print(f'part 2 total = {total}')

#part3
    if part3:
        data = readfile('/home/steve/everybodycodes/2025/Quest12/input3.txt')
        total = 0
        explored = []
        total_explored = []
        round1_explored = []
        best_start1 = [-1,-1]
        for row in range(len(data)):
            for col in range(len(data[0])):
                queue = [[row,col]]
                test_total, explored = explode_barrels(queue,data)
                test_total += 1 #(+1 for start barrel)
                if test_total > total:
                    best_start1 = [row,col]
                    round1_explored = copy.deepcopy(explored)
                    total = test_total
        total += 1  #start barrel
        total_explored += round1_explored
        print(f'part3 best first barrel is = {best_start1} with total = {total}')
        
        total = 0
        best_start2 = [-1,-1]
        queue = [0,0]
        round2_explored = []
        #set all exploded barrels from round 1 to '9' to 'remove from board'
        #for barrel in round1_explored:
        for barrel in total_explored:
             data[barrel[0]][barrel[1]] = '*'
        for row in range(len(data)):
            for col in range(len(data[0])):
                #if [row,col] not in round1_explored:
                if [row,col] in total_explored:
                    continue
                queue = [[row,col]]
                test_total, explored = explode_barrels(queue,data)
                test_total += 1 #(+1 for start barrel)
                if test_total > total:
                    best_start2 = [row,col]
                    total = test_total
                    round2_explored = copy.deepcopy(explored)
        total += 1  #add start barrel
        total_explored += round2_explored
        print(f'part3 best second barrel is = {best_start2} with total = {total}')

        total = 0
        best_start3 = [-1,-1]
        queue = [0,0]
        #round3_explored = []
        #set all exploded barrels from round 2 to '9' to 'remove from board'
        for barrel in round2_explored:
             data[barrel[0]][barrel[1]] = '*'
        for row in range(len(data)):
            for col in range(len(data[0])):
                if [row,col] in total_explored:
                    continue
                queue = [[row,col]]
                test_total, explored = explode_barrels(queue,data)
                test_total += 1 #(+1 for start barrel)
                if test_total > total:
                    best_start3 = [row,col]
                    total = test_total
                    #round3_explored = copy.deepcopy(explored)
        total += 1  #add start barrel
        print(f'part3 best third barrel is = {best_start3} with total = {total}')

        #reset data
        data = readfile('/home/steve/everybodycodes/2025/Quest12/input3.txt')
        total = 0
        queue = [best_start1,best_start2,best_start3]
        total, explored = explode_barrels(queue,data)
        total += 3   #include count of start barrel(s)
        print(f'part 3 total = {total}')


def explode_barrels(_queue,data):
    #set directions to check (ordinal N, S, E, W)
    directions = [[-1,0],[1,0],[0,1],[0,-1]]
    total = 0
    #create blank list to store barrel locations that have been exploded
    _exploded = []
    #loop while there are barrels in queue to be exploded
    while _queue != []:
        #get the next barrel of the queue
        _current_barrel = _queue.pop(0)
        #add this barrel to exploded list 
        _exploded.append(_current_barrel)
        #check barrels in directions for on map and if meet explode criteria (<= current barrel)
        for dir in directions:
            #check for out of bounds
            if _current_barrel[0] + dir[0] >= 0 and _current_barrel[0] + dir[0] < len(data) and _current_barrel[1] + dir[1] >= 0 and _current_barrel[1] + dir[1] < len(data[0]):    
                #check not already exploded - '*'
                if data[_current_barrel[0]+dir[0]][_current_barrel[1]+dir[1]] != '*':
                    #check less than or equal to current barrel and add to queue if true
                    if int(data[_current_barrel[0]+dir[0]][_current_barrel[1]+dir[1]]) <= int(data[_current_barrel[0]][_current_barrel[1]]):
                        if [_current_barrel[0]+dir[0],_current_barrel[1]+dir[1]] not in _queue and [_current_barrel[0]+dir[0],_current_barrel[1]+dir[1]] not in _exploded:
                            _queue.append([_current_barrel[0]+dir[0],_current_barrel[1]+dir[1]])
                            total += 1
    return total, _exploded




def readfile(filename):
    f = open(filename, 'r')
    _data = list()
    for line in f.readlines():
        _data.append(list(line.strip('\n')))
    return _data
    
if __name__ == '__main__':
    main()


