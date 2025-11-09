# This program is about Write into File

#Optimized way of opening n closing file

with open('test.txt', 'r') as reader:    # Automatically close when op is done.'file; is an object hence can user defined.
    lines = reader.readlines()
    reversed(lines)                     # To reverse the content in the file
    with open('test.txt', 'w') as writer:
        for l in reversed(lines):
            writer.write(l)
print("Reversed lines have been written to test.txt")

#To append more data with existing
with open('test.txt', 'a') as appender:
    appender.write("I am new appended data")

with open('test.txt', 'r') as reader:
    content = reader.read()
    print(f"Appended list = {content}")

#To append data coming at runtime
data = input("Enter data to append")
with open('test.txt', 'a') as appender:
    appender.write(f"\n{data}")

with open('test.txt', 'r') as reader:
    content = reader.read()
    print(f"Appended list = {content}")


#To append multiple lines of data
data = ["\nLine 1 added", "Line 2 added", "Line 3 added"]
with open('test.txt', 'a') as appender:
    for l in data:
        appender.write(f"{l}\n")

with open('test.txt', 'r') as reader:
    content = reader.read()
    print(f"Appended list = {content}")

