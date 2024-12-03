import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def calc(instruction):
    expr_muls = r"(mul\(\d+,\d+\))"
    muls = re.findall(expr_muls, instruction)
    
    result = 0
    expr_factors = r"mul\((\d+),(\d+)\)"
    for mul in muls:
        products = re.findall(expr_factors,mul)[0]
        result += int(products[0])*int(products[1])
    return result

def part_one():
    instruction = ""
    with open(os.path.join(__location__,"input")) as file:
        for line in file:
            instruction += line
    
    print(calc(instruction))


def part_two():
    instruction = ""
    with open(os.path.join(__location__,"input")) as file:
        for line in file:
            instruction += line

    while "don't()" in instruction:
        index_dont = -1
        index_do = -1

        index_dont = instruction.find("don't()")
        index_do = instruction.find("do()",index_dont)

        # if no do, delete everything after dont
        # else, delete everything in between

        if index_do == -1:
            instruction = instruction[:index_dont]
        else:
            instruction = instruction[:index_dont] + instruction[index_do+len("do()"):]


    print(calc(instruction))

part_one()
part_two()