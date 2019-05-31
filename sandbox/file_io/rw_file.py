# # For reading file
data = open('data.txt')
print(data.read())
data.close()

# # For reading single header or first line of file
data = open('data.txt')
print(data.readline())
data.close()

# # For reading each line iteratively and appending in a list
data = open('data.txt')
print(data.readlines())
data.close()

# For writing line in an existing file
data = open('data.txt', 'a')
data.write("\nThis is written from py program\n")
data.close()

# For writing data iteratively in file
dummy_list = [
    "Ramesh",
    "Krishna",
    "Hari",
    "Shyam",
    "Bishnu"
]
data = open('data.txt', 'w')
for i in dummy_list:
    data.writelines(
        f"{i}\n"
    )
data.close()

data = open('data.txt')
print(data.read())
data.close()

data = open('new_data.txt', 'w+')
data.write("This is first line")
data.close()