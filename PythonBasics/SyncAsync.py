#Pyhton follows by-default Synchronous execution
import asyncio
import time

#Synchronous execution
def task(name):                 #2      #7
    print(f"Starting {name}")   #3      #8
    time.sleep(2)               #4      #9
    print(f"Completed {name}")  #5      #10

# task("Shivani") #1
# task("Abhinav") #6

#Asynchrounous execution
async def task(name):           #2      #6
    print(f"Starting {name}")   #3      #7
    await asyncio.sleep(2)      #4 (wait 2sec for task("Shivani"), but immediately control transfers to task("Abhinav")  #8
    print(f"Completed {name}")  #9 (Completed Shivani)  #10 (Completed Abhinav)


async def main():
    await asyncio.gather(task("Shivani"),   #1
                         task("Abhinav"))   #5

asyncio.run(main())
