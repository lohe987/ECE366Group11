import collections

def instr_load(line):
    # 000 RX RY
    if line[0] != "load":
        return "ERROR LINE CANNOT BE PARSED"
    else:
        return "000" + registers.get(line[1], "??") + registers.get(line[2], "??")

def instr_store(line):
    # 001 RX RY
    if line[0] != "store":
        return "ERROR LINE CANNOT BE PARSED"
    else:
        return "001" + registers.get(line[1], "??") + registers.get(line[2], "??")

def instr_add(line):
    # 010 RX RY
    if line[0] != "add":
        return "ERROR LINE CANNOT BE PARSED"
    else:
        return "010" + registers.get(line[1], "??") + registers.get(line[2], "??")

def instr_branch(line):
    # 011 RX RY
    if line[0] != "branch":
        return "ERROR LINE CANNOT BE PARSED"
    else:
        return "011" + registers.get(line[1], "??") + registers.get(line[2], "??")

def instr_jump(line):
    # 100 iiii
    return "NOT COMPLETE"

def instr_init(line):
    # 101 RR ii
    return "NOT COMPLETE"

def instr_slr(line):
    # 110 00 RR
    return "NOT COMPLETE"

def instr_and(line):
    # 110 01 RR
    return "NOT COMPLETE"

def instr_sll(line):
    # 110 10 RR
    return "NOT COMPLETE"

def add_praity_bit(encoded_line):
    # Adds even parity bit to encoded_line
    # Count the number of zeros and ones in the encoded line
    one_zero_dict = collections.Counter(encoded_line)
    # If number of ones is odd at 1 as the parity bit
    if one_zero_dict["1"] % 2 == 1:
        return "1" + encoded_line
    else:
        return "0" + encoded_line

instructions = {"load" : instr_load,
               "store" : instr_store,
               "add" : instr_add,
               "branch" : instr_branch,
               "jump" : instr_jump,
               "init" : instr_slr,
               "and" : instr_and,
               "sll" : instr_sll,
               "slr" : instr_slr}

registers = {"R0" : "00",
             "R1" : "01",
             "R2" : "10",
             "R3" : "11"}


if __name__ == "__main__":
    print("Testing program")
    line = "load R0, R1"
    line = line.replace(",","")
    line = line.split(" ")
    print(line)
    print(instructions["load"](line))
