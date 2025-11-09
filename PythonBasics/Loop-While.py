# This program is about While loop

it = 10
while it>1:                 # Executes till condition is TRUE, the moment it becomes FALSE, loop completed
    if it == 9:
        it -= 1
        print("Condition met, hence 9 will not be printed. It will run for 8.")
        continue            # When condition met, stop the current execution , n continue with next execution in the loop.
    if it == 3:
        print("Condition met, hence loop broke.")
        break               # When condition met, break the whole loop, n come out of it.
    print(it)
    it -= 1

print("While loop execution completed !!")
