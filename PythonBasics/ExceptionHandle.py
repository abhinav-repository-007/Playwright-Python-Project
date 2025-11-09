with open('test.txt', 'w') as f:
    f.write('hello world')    #Read whole content in the file


try:
    with open('test.txt', 'r') as f:
        print(f.read())

# If something is failing with try block, then it will not stop the execution abruptly there,
    # it will catch the error and goto except block and save in Exception class and then print
except Exception as e:
    print(e)

finally:
    print("I will be executed irrespective of failing of either try/except. hence use me for Close db connection, or clean up the resource")