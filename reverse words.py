def reverse_words(s):
    words = s.strip().split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
input_string = input("Enter a string: ")
result = reverse_words(input_string)
print("Reversed words:", result)
