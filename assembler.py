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
    # 110 10 RR
    return "110" + "10" + registers.get(line[1], "??")

def instr_init(line):
    # 101 RR ii
    return "101" + registers.get(line[1], "??") + convert_imm_value(line[2])[-2:]

def instr_slr(line):
    # 110 00 RR
    return "110" + "00" + registers.get(line[1], "??")

def instr_and(line):
    # 110 01 RR
    return "110" + "01" + registers.get(line[1], "??")

def instr_slt(line):
    # 100 RX RY
    return "100" + registers.get(line[1], "??") + registers.get(line[2], "??")

def instr_xor(line):
    # 111 RR RR
    return "111" + registers.get(line[1], "??") + registers.get(line[2], "??")

def instr_not(line):
    # 110 11 RR
    return "110" + "11" + registers.get(line[1], "??")

def add_praity_bit(encoded_line):
    # Adds even parity bit to encoded_line
    # Count the number of zeros and ones in the encoded line
    one_zero_dict = collections.Counter(encoded_line)
    # If number of ones is odd at 1 as the parity bit
    if one_zero_dict["1"] % 2 == 1:
        return "1" + encoded_line
    else:
        return "0" + encoded_line

def convert_imm_value(number):
    if int(number) < 0:
        number = 0xFFFF - int(number[1:]) + 1
    return format(int(number), "016b")

def assemble_file(input_file_name="CTZ_instructions.txt", output_file_name="CTZ_machine_code.txt"):
    # Open files using default args or user provided
    input_file = open(input_file_name, "r")
    output_file = open(output_file_name, "w")

    # For each line in input file process the function
    for line in input_file:
        # Remove comments from code
        if line.startswith("#"):
            continue
        line = line.replace(",", "")
        line = line.replace("\n", "")
        line = line.split(" ")
        func = instructions.get(line[0], "?")
        # Check if function is known if not print error messafe
        if func == "?":
            output_file.write("UNKNOWN\n")
        else:
            # Encode function then add praity bit
            encoded = add_praity_bit(func(line)) + "\n"
            output_file.write(encoded)

    input_file.close()
    output_file.close()



instructions = {"load" : instr_load,
               "store" : instr_store,
               "add" : instr_add,
               "branch" : instr_branch,
               "jump" : instr_jump,
               "init" : instr_init,
               "and" : instr_and,
               "slt" : instr_slt,
               "slr" : instr_slr,
               "not" : instr_not,
               "xor" : instr_xor}

registers = {"R0" : "00",
             "R1" : "01",
             "R2" : "10",
             "R3" : "11"}


if __name__ == "__main__":
    assemble_file()
