# This program is about List operations
# List is DT, can have multiple values of either same or different DTs

value = [1, 2.3, "shivani", 5, 9]
print(value)                                # [1, 2.3, 'shivani', 5, 9]
print(type(value))                          # <class 'list'>
print(len(value))                           # 5
print(value[0])                             # 1
print(value[2])                             # shivani
print(value[-1])                            # Last value in list = 9
print(value[1:3])                           # Range, but exclude place 3 = [2.3, 'shivani']
value.insert(3, "hello")    # Insert value in-between
value.append("world")                       # Add value at end
value[2] = "SHIVANI"                        # Replace
del value[3]                                # Delete any value
print(value)                                # [1, 2.3, 'SHIVANI', 5, 9, 'world']
