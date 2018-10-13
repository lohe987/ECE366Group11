# Class CPU will hold the information of the CPU
class CPU:
    PC = 0 # Program Counter
    DIC = 0 # Insturction Counter
    R = [0] * 4 # Register Values
    instructions = [] # instructions in array
    memory = [] # memory in array

def check_parity_bit(machine_line):
    # Count the number of zeros and ones
    one_zero_dict = collections.Counter(machine_line)
    # Make sure an even number of ones exist in the instructions
    if one_zero_dict["1"] % 2 == 0:
        return True
    return False

def load_program(cpu, instr_file_name, memory_file_name):
    instr_file = open(instr_file_name, "r")
    memory_file = open(memory_file_name, "r")

    for line in instr_file:
        line = line.strip()
        if len(line) < 1 or line.startswith("#"):
            continue
        cpu.instructions.append(line)

    for line in memory_file:
        line = line.strip()
        if len(line) < 1 or line.startswith("#"):
            continue
        cpu.memory.append(int(line,2))

    for i in range(128-len(cpu.memory)):
        cpu.memory.append(0)

    instr_file.close()
    memory_file.close()

    return cpu

if __name__ == "__main__":
    cpu1 = CPU()
    cpu1 = load_program(cpu1, "sample_program_machine.ctz", "sample_memory.txt")
    print(cpu1.memory[0:5])
