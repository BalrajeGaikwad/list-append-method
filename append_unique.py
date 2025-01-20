#Append unique elements only

unique_elements = []
for i in range(1, 11):
    if i not in unique_elements:
        unique_elements.append(i)
print("Unique elements:", unique_elements)


string = "Hello"
char_list = []
for char in string:
    char_list.append(char)
print("List of characters in the string:", char_list)
