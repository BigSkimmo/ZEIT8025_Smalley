from subprocess import Popen, PIPE
proc = Popen('C:\\Users\\Simmo\\Desktop\\ReverseEngBinaries\\BinaryA.exe', stdin=PIPE)
print(proc.communicate(b'\xa9'))
