# This program is about For loop
value = [1, 2.5, "shivani", 24324]
for i in value:
    print(i)                            # 1   2.5   "shivani"   24324
print("**************************************************************")

# Print first 5 natural nos.
for j in range(1, 6):
    print(j)                            # 1   2    3    4    5
print("**************************************************************")

# Sum of 1+2+3+4+5 = 15
summation = 0
for k in range(1, 6):
    summation += k
print("summation = ", summation)        # summation =  15
print("**************************************************************")

# Skipping value by 2
for m in range(1, 10, 2):   # 3rd arg is to say skip by 2
    print(m)                            # 1  3  5  7  9

print("**************************************************************")
# By default starting with 0th index
for n in range(10):
    print(n)                            # 0  1  2  3  4  5  6  7  8  9

