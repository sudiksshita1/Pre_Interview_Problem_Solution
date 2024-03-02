from util import swapNumbers
import threading
from util.palindrome import Integer

#input for swap numbers
with open('inputs/inputForProgram1.txt', 'r') as file:
    input1 = list(map(int, file.readline().split()))

with open('inputs/inputForProgram2.txt', 'r') as file:
        input2 = int(file.readline())

def thread_operation1():
    swapNumbers.swap_variables(input1)

def thread_operation2():
    n = Integer(input2)
    if n.is_palindrome():
        print(input2, " is a palindrome")
    else:
        print(input2, " is not a palindrome")


t1 = threading.Thread(target=thread_operation1)
t2 = threading.Thread(target=thread_operation2)

print("Numbers before swap: ", input1)
t1.start()
print("Numbers after swap: ",input1)

t2.start()

t1.join()
t2.join()

