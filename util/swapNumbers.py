# Swapping the values of a and b using reference passing
def swap_variables(list):
    if len(list) >= 2:
     list[0], list[1] = list[1], list[0]
if __name__ == "__main__":
    with open('inputForProgram1.txt', 'r') as file:    
       my_list = [int(x) for x in file.readline().split()]
       print("Before swapping:")
       print("list[0] =", list[0])
       print("list[1] =", list[1])   

    swap_variables(my_list)

    print("After swapping:")
    print("list[0] =", list[1])
    print("list[1] =", list[0])