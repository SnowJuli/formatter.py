import time
from subprocess import Popen, PIPE

p = Popen(["diskpart"], stdin=PIPE, shell=True)
print("try 1")
done1 = p.stdin.write(bytes("list disk", 'utf-8'))
print("try 2")
print(done1)
