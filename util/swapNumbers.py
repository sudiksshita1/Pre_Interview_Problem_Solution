# Swapping the values of a and b using reference passing
#def swap_variables(list):
    #list[0], list[1] = list[1], list[0]
    #list[0], list[1] = list[1], list[0]
def swap_variables(a, b):
    a,b = b, a
if __name__ == "__main__":
    print("Before swapping:")
    print("a =", a)
    print("b =", b)

swap_variables(a, b)

print("After swapping:")
print("a =", a)
print("b =", b)