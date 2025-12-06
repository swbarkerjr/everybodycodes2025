def main():
    data = readfile('/home/steve/everybodycodes/2025/Quest11/pt3.txt')
    flock = list()
    target_rounds = -1
    for item in data:
        flock.append(int(item.strip('\n')))
    flock, rounds, checksum = phase1(flock)
#    print(f'phase1 final: flock={flock}, rounds={rounds}, checksum={checksum}')
    print(f'part3 total rounds = {rounds + part3(flock)}')    
#    flock, rounds, checksum = phase2(flock,rounds,target_rounds)
#    print(f'phase2 final: flock={flock}, rounds={rounds}, checksum={checksum}')
    



def phase1(_flock:list):
    _stop_phase1_flag = False
    _round = 0
    if sorted(_flock) == _flock:
        return _flock, 0, checksum(_flock)
    while not _stop_phase1_flag:
        _round += 1
        for index in range(len(_flock)-1):
            if _flock[index] > _flock[index+1]:
                _flock[index] -= 1
                _flock[index+1] += 1
                
                continue
            if sorted(_flock) == _flock:
                _stop_phase1_flag = True
        #print(f'phase1: round {_round}, flock {_flock}, checksum {checksum(_flock)}')
    return _flock, _round, checksum(_flock)  


def phase2(_flock:list,_round:int, _target_rounds:int):
    _stop_phase2_flag = False
    while not _stop_phase2_flag:
        _round += 1
        for index in range(len(_flock)-1):
            if _flock[index+1] > _flock[index]:
                _flock[index+1] -= 1
                _flock[index] += 1
                continue
            if _flock[0] == _flock[-1]:
                _stop_phase2_flag = True
        #print(f'phase2: round {_round}, flock {_flock}, checksum {checksum(_flock)}')
        if _round == _target_rounds:
            _stop_phase2_flag = True
    return _flock, _round, checksum(_flock)

def part3(_flock):
    _avg = int(sum(_flock)/len(_flock))
    _total = 0
    for item in _flock:
        if item > _avg:
            _total += item - _avg
    return _total

def checksum(_flock):
    _checksum = 0
    for i,num in enumerate(_flock):
        _checksum += (i+1) * num
    return _checksum

def readfile(filename):
    f = open(filename, 'r')
    return f.readlines()
    
if __name__ == '__main__':
    main()


