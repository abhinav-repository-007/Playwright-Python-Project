# This program is about Read File content
# Create 1 file = text.txt, add some data

File = open('test.txt')     # Open file

# Its mandate to use only 1 read() with/ without Char count.
#print(File.read())          # Read content of file = Shivani   Abhinav   Rajdeep    Runjhun
#print(File.read(4))          # Read 4 Char = Shiv
# print(File.readline())          # Read 1st line = Shivani
# print(File.readline())          # Read 2nd line = Abhinav

# File = open('test.txt')     # Open file
# Read multiple line using readline() with loop
# line = File.readline()
# while line!="":
#     print(line)
#     line = File.readline()


# Difference between readline() & readlines() => readlines() takes line content into list
lines = File.readlines()
print(lines)                # ['Shivani\n', 'Abhinav\n', 'Rajdeep\n', 'Runjhun']
for line in lines:
    print(line)

File.close()                # When open file, mandate to close to avoid memory leak

