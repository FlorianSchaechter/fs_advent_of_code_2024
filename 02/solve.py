import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def test_increments(items):
    # Test for increments
    for i in range(len(items)-1):
        if abs(items[i]-items[i+1]) > 3:
            return False
        
    return True

def test_direction(items):
    # create a hypothesis for asc or desc
    asc =  items[0] < items[-1]

    # Test if strictly descending or ascending
    if asc:
        for i in range(len(items)-1):
            if items[i+1] <= items[i]:
                return False
    else:
        for i in range(len(items)-1):
            if items[i+1] >= items[i]:
                return False
            
    return True


def part_one():
    num_safe = 0

    with open(os.path.join(__location__,"input")) as file:
        for line in file:
            line = [int(x) for x in line.split()]

            increments_ok = test_increments(line)
            direction_ok = test_direction(line)

            if direction_ok and increments_ok:
                num_safe += 1

    print(num_safe)

def part_two():
    num_safe = 0

    with open(os.path.join(__location__,"input")) as file:
        for line in file:
            line = [int(x) for x in line.split()]

            orignal_line = line.copy()

            for i in range(len(orignal_line)):
                line = orignal_line[:i] + orignal_line[i+1:]
                increments_ok = test_increments(line)
                direction_ok = test_direction(line)

                if direction_ok and increments_ok:
                    num_safe += 1
                    break

    print(num_safe)

part_one()
part_two()