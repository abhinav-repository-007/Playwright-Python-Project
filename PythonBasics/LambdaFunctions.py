# Use of map() with lambda

numbers = [1,2,3,4,5]

squared_numbers = map(lambda i: i*2, numbers)

print(list(squared_numbers))

# Use of filter() with lambda
# Filter even num from numbers[]

even_num = list(filter(lambda x : x % 2 == 0, numbers))
print(even_num)