import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def part_one():
    instruction = ""
    with open(os.path.join(__location__,"input")) as file:
        for line in file:
            instruction += line
            
    expr_muls = r"(mul\(\d+,\d+\))"
    muls = re.findall(expr_muls, instruction)
    
    result = 0
    expr_factors = r"mul\((\d+),(\d+)\)"
    for mul in muls:
        products = re.findall(expr_factors,mul)[0]
        result += int(products[0])*int(products[1])
    print (result)

def part_two():
    with open(os.path.join(__location__,"input")) as file:
        for line in file:
            yield

part_one()
part_two()