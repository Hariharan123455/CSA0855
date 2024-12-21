def add_binary(a, b):
    
    return bin(int(a, 2) + int(b, 2))[2:]
    
# Input from user
a = input("Enter the first binary string: ")
b = input("Enter the second binary string: ")

# Output the result
print("The sum of the binary strings is:",add_binary(a,b))
