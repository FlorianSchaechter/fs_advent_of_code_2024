import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def part_one():
    # two lists
    left = []
    right = []
    distance = 0

    with open(os.path.join(__location__,"input")) as file:
        for line in file:
            line = line.split()
            left.append(int(line[0])) 
            right.append(int(line[1]))

    left.sort()
    right.sort()

    for i in range(len(left)):
        distance += abs(left[i]-right[i])

    print(distance)

def part_two():
    left = []
    right = []
    similartiy = 0


    with open(os.path.join(__location__,"input")) as file:
        for line in file:
            line = line.split()
            left.append(int(line[0])) 
            right.append(int(line[1]))

    count_dict = {i:right.count(i) for i in right}

    for i in left:
        if i in count_dict:
            similartiy += i * count_dict[i]
    
    print(similartiy)

part_one()
part_two()