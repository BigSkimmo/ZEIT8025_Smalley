import sys
from subprocess import Popen, PIPE

def make_choice(arg):
    switch = { '1': b'\x64', '2': b'\x65', '3': b'\x70', '4': b'\xa9' }

    binaries = { '1': 'C:\\Users\\Simmo\\Desktop\\ReverseEngBinaries\\BinaryA.exe',
                 '2': 'C:\\Users\\Simmo\\Desktop\\ReverseEngBinaries\\BinaryB.exe' }

    while True:
        choice = input("$> ")
        if arg == 'binary':
            ret = binaries.get(choice)
            if ret != None:
                return ret
        elif arg == 'input':
            ret = switch.get(choice)
            if ret != None:
                return ret
        print("Invalid input")

def conditions(procname):
    BinAConditions = ['"Ops! not this one"','"Ops! not this one"','"Ops! there are more"','"Ops! you may have found the key!"']
    BinBConditions = ['"Ops! not this one"','"Ops! there are more"','"Ops! not this one"','"Ops! you may have found the key!"']
    if procname == 'BinaryA.exe':
        return BinAConditions
    elif procname == 'BinaryB.exe':
        return BinBConditions
    else:
        print("Could not identify binary!")
        sys.exit(1)

def main():
    print("Pick binary to interact with:")
    print("1: BinaryA.exe")
    print("2: BinaryB.exe")

    try:
        proc = Popen(make_choice('binary'), stdin=PIPE)
        flow = conditions(proc.args.split("\\")[5])
    except:
        print('Unable to open binary!')
        sys.exit(1)

    print("Pick input for process:")
    print("1: [d] (0x64) - Enters", flow[0], "condition")
    print("2: [e] (0x65) - Enters", flow[1], "condition")
    print("3: [p] (0x70) - Enters", flow[2], "condition")
    print("4: [no ascii] (0xA9) - Enters", flow[3], "condition")

    print(proc.communicate(make_choice('input')))

if __name__ == '__main__':
    main()
