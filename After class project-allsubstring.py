def all_substrings(s):
    substrings = []
    length = len(s)
    for i in range(length):
        for j in range(i+1, length+1):
            substrings.append(s[i:j])
    return substrings

string = input("Enter a string: ")
result = all_substrings(string)

print("All substrings:")
for substr in result:
    print(substr)