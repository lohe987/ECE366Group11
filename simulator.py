# Class CPU will hold the information of the CPU
class CPU:
    pc = 0 # Program Counter
    DIC = 0 # Insturction Counter
    R = [0] * 4 # Register Values
    instructions = None # instructions in array
    memory = None # memory in array


if __name__ == "__main__":
    cpu1 = CPU()
    print(CPU.R)
