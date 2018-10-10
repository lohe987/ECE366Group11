import collections

def check_parity_bit(machine_line):
    # Count the number of zeros and ones
    one_zero_dict = collections.Counter(machine_line)
    # Make sure an even number of ones exist in the instructions
    if one_zero_dict["1"] % 2 == 0:
        return True
    return False

def determine_function(machine_line):
    if machine_line[1:4] == "110":
        return single_register(machine_line)
    elif machine_line[1:4] == "101":
        return imm_value(machine_line)
    else:
        return double_register(machine_line)

def single_register(machine_line):
    op_code = {"10" : "jump",
               "00" : "slr",
               "01" : "and",
               "11" : "not"}
    # Determine function code
    asm_line = op_code.get(machine_line[4:6], "UNKNOWN")
    # Add register values
    asm_line += " " + registers.get(machine_line[6:8], "??")
    return asm_line

def imm_value(machine_line):
    value = {"11" : "-2",
             "10" : "-1",
             "00" : "0",
             "01" : "1"}
    # Add function word and register
    asm_line = "init" + " " + registers.get(machine_line[4:6], "??") + ", "
    # Find imm value in table
    asm_line += value.get(machine_line[6:8], "??")
    return asm_line

def double_register(machine_line):
    func_code = {"000" : "load",
                 "001" : "store",
                 "010" : "add",
                 "011" : "beq",
                 "100" : "slt",
                 "111" : "xor"}
    # Add function code to begining of assembler line
    asm_line = func_code.get(machine_line[1:4], "UNKNOWN")
    # Update with register values
    asm_line += " " + registers.get(machine_line[4:6], "??") + ", " + registers.get(machine_line[6:8], "??")
    return asm_line

def disassemble_file(input_file_name="CTZ_machine_code.txt", output_file_name="CTZ_instructions_decoded.txt"):
    # Open files using default args or user provided
    input_file = open(input_file_name, "r")
    output_file = open(output_file_name, "w")

    # For each line in input file process the function
    for line in input_file:
        # Remove new line for line
        line = line.replace("\n", "")
        if check_parity_bit(line):
            asm_line = determine_function(line)
        else:
            asm_line = "PARITY ERROR"

        output_file.write(asm_line + "\n")

    input_file.close()
    output_file.close()

registers = {"00" : "R0",
             "01" : "R1",
             "10" : "R2",
             "11" : "R3"}

if __name__ == "__main__":
    disassemble_file()
